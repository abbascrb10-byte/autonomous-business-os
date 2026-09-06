from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.domain.signals import DemandSignal
from app.sources.deduplication import DeduplicationService
from app.database.models import DBDemandSignal
from app.graph.workflow import gpie_graph

router = APIRouter()

@router.post("/signals/ingest")
async def ingest_signal(signal: DemandSignal, db: Session = Depends(get_db)):
    if DeduplicationService.is_duplicate(db, signal):
        return {"status": "DUPLICATE", "message": "Signal already ingested"}

    db_sig = DBDemandSignal(
        source=signal.source,
        source_id=signal.source_id,
        raw_text=signal.raw_text,
        author_reference=signal.author_reference,
        country=signal.country,
        fingerprint=signal.fingerprint
    )
    db.add(db_sig)
    db.commit()
    db.refresh(db_sig)
    return {"status": "INGESTED", "signal_id": db_sig.signal_id}

@router.post("/workflow/run")
async def run_workflow(signal: DemandSignal, user_response: str = ""):
    initial_state = {
        "signal": signal,
        "intent": None,
        "requirements": None,
        "offers": [],
        "best_offer": None,
        "policy_allowed": False,
        "contact": None,
        "permission_message": None,
        "offer_message": None,
        "user_response": user_response,
        "status": "START"
    }
    result = await gpie_graph.ainvoke(initial_state)
    return {
        "status": result.get("status"),
        "intent": result.get("intent"),
        "best_offer": result.get("best_offer"),
        "permission_message": result.get("permission_message"),
        "offer_message": result.get("offer_message")
    }
