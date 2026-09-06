from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class AnalyticsEvent(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    event_id: Optional[str] = None
    event_type: str
    entity_id: Optional[str] = None
    data: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
