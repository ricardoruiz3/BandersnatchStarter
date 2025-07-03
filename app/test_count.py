from data import Database

if __name__ == "__main__":
    db = Database()
    count = db.count()
    print(f"There are {count} monsters in the collection.")
