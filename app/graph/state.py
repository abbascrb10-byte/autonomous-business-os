from typing import TypedDict, Optional, List, Dict, Any
from app.domain.signals import DemandSignal
from app.domain.intents import PurchaseIntent, ExtractedProductRequirements
from app.domain.offers import Offer
from app.domain.contacts import Contact
from app.domain.contacts import OutreachMessage

class GPIEGraphState(TypedDict):
    signal: DemandSignal
    intent: Optional[PurchaseIntent]
    requirements: Optional[ExtractedProductRequirements]
    offers: List[Offer]
    best_offer: Optional[Offer]
    policy_allowed: bool
    contact: Optional[Contact]
    permission_message: Optional[OutreachMessage]
    offer_message: Optional[OutreachMessage]
    user_response: Optional[str]
    status: str
