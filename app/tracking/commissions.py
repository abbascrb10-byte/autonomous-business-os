from datetime import datetime
from sqlalchemy.orm import Session
from app.database.models import DBAnalyticsEvent

class CommissionTracker:
    @staticmethod
    def record_commission(db: Session, offer_id: str, commission_amount: float) -> DBAnalyticsEvent:
        event = DBAnalyticsEvent(
            event_type="COMMISSION",
            entity_id=offer_id,
            event_data={"commission_amount": commission_amount},
            timestamp=datetime.utcnow()
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event
