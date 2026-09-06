from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class ExtractedProductRequirements(BaseModel):
    product_name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    category: Optional[str] = None
    budget: Optional[float] = None
    currency: Optional[str] = "USD"
    destination_country: Optional[str] = "US"
    specifications: List[str] = Field(default_factory=list)
    timeframe: Optional[str] = None

class PurchaseIntent(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    intent_id: Optional[str] = None
    signal_id: str
    intent_score: float = Field(ge=0.0, le=100.0)
    requirements: ExtractedProductRequirements
    qualified: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
