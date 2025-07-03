from data import Database

if __name__ == "__main__":
    db = Database()
    inserted_ids = db.seed(5)
    print(f"Inserted {len(inserted_ids)} documents.")
