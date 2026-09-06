from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class DemandSignal(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    signal_id: Optional[str] = None
    source: str
    source_id: str
    raw_text: str
    url: Optional[str] = None
    author_reference: Optional[str] = None
    country: Optional[str] = "US"
    language: Optional[str] = "en"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    fingerprint: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
