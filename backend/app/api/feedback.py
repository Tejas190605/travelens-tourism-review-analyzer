from collections import defaultdict
import time
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Destination, IssueReport, User
from app.api.auth import get_current_admin
from app.schemas.feedback import IssueReportCreate, IssueReportResponse, IssueReportOut

router = APIRouter(prefix="/feedback", tags=["Feedback"])

VALID_ISSUE_TYPES = [
    "Outdated price or opening hours",
    "Inaccurate attraction description",
    "Misrepresented aspect feedback",
    "Transit or location discrepancy",
    "Broken image or link",
    "Other data discrepancy"
]

# In-memory sliding window rate limiter: 10 requests per minute per IP
_ip_request_timestamps = defaultdict(list)
RATE_LIMIT_WINDOW_SEC = 60
MAX_REQUESTS_PER_WINDOW = 10

def enforce_rate_limit(request: Request):
    client_ip = request.client.host if request.client else "127.0.0.1"
    now = time.time()
    _ip_request_timestamps[client_ip] = [
        t for t in _ip_request_timestamps[client_ip] if now - t < RATE_LIMIT_WINDOW_SEC
    ]
    if len(_ip_request_timestamps[client_ip]) >= MAX_REQUESTS_PER_WINDOW:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please wait a minute before submitting another issue report."
        )
    _ip_request_timestamps[client_ip].append(now)

@router.post("/report", response_model=IssueReportResponse, status_code=status.HTTP_201_CREATED)
def submit_issue_report(
    payload: IssueReportCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Submits an information issue report regarding a destination.
    Persisted to database for operator auditing. Rate-limited per IP.
    """
    enforce_rate_limit(request)

    # 1. Verify destination exists
    destination = db.query(Destination).filter(Destination.id == payload.destination_id).first()
    if not destination:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with id {payload.destination_id} does not exist"
        )

    # 2. Validate issue type
    issue_type = payload.issue_type.strip()
    if len(issue_type) < 3 or len(issue_type) > 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Issue type must be between 3 and 100 characters"
        )

    comment = payload.comment.strip() if payload.comment else None
    if comment and len(comment) > 1000:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Comment cannot exceed 1000 characters"
        )

    contact_email = payload.contact_email.strip() if payload.contact_email else None
    if contact_email and len(contact_email) > 255:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Contact email cannot exceed 255 characters"
        )

    # 3. Create report
    report = IssueReport(
        destination_id=payload.destination_id,
        issue_type=issue_type,
        comment=comment,
        contact_email=contact_email,
        status="open"
    )
    db.add(report)
    db.commit()
    db.refresh(report)

    return IssueReportResponse(
        status="success",
        message="Thank you for contributing to data integrity. Your report has been recorded.",
        report_id=report.id
    )

@router.get("/reports", response_model=List[IssueReportOut])
def get_issue_reports(
    current_admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    """
    Restricted endpoint: Retrieves submitted issue reports for authorized operators only.
    """
    return db.query(IssueReport).order_by(IssueReport.created_at.desc()).all()
