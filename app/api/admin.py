from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.database.models import DBDemandSignal, DBPurchaseIntent, DBAnalyticsEvent

router = APIRouter()

@router.get("/admin/stats")
def admin_stats(db: Session = Depends(get_db)):
    signals_count = db.query(DBDemandSignal).count()
    intents_count = db.query(DBPurchaseIntent).count()
    events_count = db.query(DBAnalyticsEvent).count()
    return {
        "total_signals": signals_count,
        "total_intents": intents_count,
        "total_analytics_events": events_count
    }
