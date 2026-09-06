from typing import List
from datetime import datetime
from app.sources.base import BaseSourceAdapter
from app.domain.signals import DemandSignal

class AgenticSourceAdapter(BaseSourceAdapter):
    def __init__(self):
        super().__init__(source_name="agentic")

    async def fetch_signals(self) -> List[DemandSignal]:
        return [
            DemandSignal(
                source=self.source_name,
                source_id="agent_msg_88",
                raw_text="Buyer Agent requesting quote for Dell XPS 15 laptop under $1800",
                author_reference="buyer_agent_alpha",
                country="US",
                timestamp=datetime.utcnow()
            )
        ]
