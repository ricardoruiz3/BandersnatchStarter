from app.data import Database

if __name__ == "__main__":
    db = Database()
    inserted_ids = db.seed(1000)
    print(f"Seeded {len(inserted_ids)} monsters.")
