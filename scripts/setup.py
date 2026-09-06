from app.database.session import init_db

def main():
    print("Initializing GPIE Database...")
    init_db()
    print("Database initialization complete.")

if __name__ == "__main__":
    main()
