from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: Optional[str] = None
    title: str
    brand: Optional[str] = None
    model: Optional[str] = None
    category: Optional[str] = None
    specifications: Dict[str, Any] = Field(default_factory=dict)

class Offer(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    offer_id: Optional[str] = None
    product_id: str
    merchant: str
    title: str
    price: float
    currency: str = "USD"
    in_stock: bool = True
    seller: Optional[str] = None
    shipping_destination: Optional[str] = None
    shipping_cost: float = 0.0
    rating: Optional[float] = None
    affiliate_url: str
    commission_rate: float = 0.0
    rank_score: Optional[float] = None
    verified: bool = False
