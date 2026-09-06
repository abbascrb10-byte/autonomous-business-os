from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class Contact(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    contact_id: Optional[str] = None
    source: str
    author_reference: str
    channel: str
    permission_granted: bool = False
    opted_out: bool = False
    last_contacted_at: Optional[datetime] = None

class OutreachMessage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    message_id: Optional[str] = None
    intent_id: str
    contact_id: str
    message_type: str  # "PERMISSION_REQUEST" or "COMMERCIAL_OFFER"
    body: str
    sent_at: datetime = Field(default_factory=datetime.utcnow)
    response_received: Optional[str] = None
