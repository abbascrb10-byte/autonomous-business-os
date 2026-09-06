from abc import ABC, abstractmethod
from typing import List
from app.domain.offers import Offer
from app.domain.intents import ExtractedProductRequirements

class BaseMerchantAdapter(ABC):
    def __init__(self, merchant_name: str):
        self.merchant_name = merchant_name

    @abstractmethod
    async def search_offers(self, requirements: ExtractedProductRequirements) -> List[Offer]:
        """Search merchant catalog for offers matching extracted requirements."""
        pass
