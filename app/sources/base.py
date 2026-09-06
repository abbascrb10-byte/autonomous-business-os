from abc import ABC, abstractmethod
from typing import List
from app.domain.signals import DemandSignal

class BaseSourceAdapter(ABC):
    def __init__(self, source_name: str):
        self.source_name = source_name

    @abstractmethod
    async def fetch_signals(self) -> List[DemandSignal]:
        """Fetch purchase demand signals from source."""
        pass
