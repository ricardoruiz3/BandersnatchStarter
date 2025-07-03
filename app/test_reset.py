from data import Database

if __name__ == "__main__":
    db = Database()
    deleted_count = db.reset()
    print(f"Deleted {deleted_count} documents from the collection.")
