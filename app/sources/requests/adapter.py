from typing import List
from datetime import datetime
from app.sources.base import BaseSourceAdapter
from app.domain.signals import DemandSignal

class RequestsSourceAdapter(BaseSourceAdapter):
    def __init__(self):
        super().__init__(source_name="requests")

    async def fetch_signals(self) -> List[DemandSignal]:
        # Explicit purchase requests feed/mock ingestion
        return [
            DemandSignal(
                source=self.source_name,
                source_id="req_101",
                raw_text="I need a Sony A7 IV camera under $2000 shipped to US this week.",
                author_reference="user_alex",
                country="US",
                timestamp=datetime.utcnow()
            )
        ]
