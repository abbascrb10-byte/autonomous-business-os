import asyncio
from app.database.session import SessionLocal
from app.database.models import DBDemandSignal, DBPurchaseIntent
from app.agents.intent_agent import IntentAgent
from app.domain.signals import DemandSignal

async def run_classification_worker():
    db = SessionLocal()
    unclassified_signals = db.query(DBDemandSignal).filter(
        ~DBDemandSignal.intents.any()
    ).all()

    classified_count = 0
    for db_sig in unclassified_signals:
        sig = DemandSignal.model_validate(db_sig)
        intent = IntentAgent.classify_intent(sig)

        db_intent = DBPurchaseIntent(
            signal_id=db_sig.signal_id,
            intent_score=intent.intent_score,
            extracted_requirements=intent.requirements.model_dump(),
            qualified=intent.qualified
        )
        db.add(db_intent)
        classified_count += 1

    db.commit()
    db.close()
    return classified_count
