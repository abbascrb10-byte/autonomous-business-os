from app.database.session import SessionLocal, init_db
from app.database.models import DBDemandSignal

def seed_data():
    init_db()
    db = SessionLocal()
    if db.query(DBDemandSignal).count() == 0:
        sig = DBDemandSignal(
            source="requests",
            source_id="seed_1",
            raw_text="I need to buy a Sony A7 IV camera under $2000 shipped to US",
            author_reference="seed_user"
        )
        db.add(sig)
        db.commit()
        print("Seed data inserted.")
    else:
        print("Database already contains data.")
    db.close()

if __name__ == "__main__":
    seed_data()
