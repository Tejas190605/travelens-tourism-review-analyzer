from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class IssueReportCreate(BaseModel):
    destination_id: int = Field(..., description="Destination ID being reported")
    issue_type: str = Field(..., min_length=3, max_length=100, description="Category of reported issue")
    comment: Optional[str] = Field(None, max_length=1000, description="Optional explanation or context")
    contact_email: Optional[str] = Field(None, max_length=255, description="Optional contact email for follow-up")

class IssueReportResponse(BaseModel):
    status: str
    message: str
    report_id: int

class IssueReportOut(BaseModel):
    id: int
    destination_id: int
    issue_type: str
    comment: Optional[str] = None
    contact_email: Optional[str] = None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

