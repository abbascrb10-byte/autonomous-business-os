from typing import List
from datetime import datetime
from app.sources.base import BaseSourceAdapter
from app.domain.signals import DemandSignal

class OwnedSourceAdapter(BaseSourceAdapter):
    def __init__(self):
        super().__init__(source_name="owned")

    async def fetch_signals(self) -> List[DemandSignal]:
        return []

    async def ingest_user_request(self, text: str, user_ref: str, country: str = "US") -> DemandSignal:
        return DemandSignal(
            source=self.source_name,
            source_id=f"owned_{int(datetime.utcnow().timestamp())}",
            raw_text=text,
            author_reference=user_ref,
            country=country,
            timestamp=datetime.utcnow()
        )
