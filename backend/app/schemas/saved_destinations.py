from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.destination import DestinationOut

class SavedDestinationOut(BaseModel):
    id: int
    user_id: int
    destination_id: int
    created_at: datetime
    destination: DestinationOut

    model_config = ConfigDict(from_attributes=True)

class SavedStatusResponse(BaseModel):
    destination_id: int
    is_saved: bool
