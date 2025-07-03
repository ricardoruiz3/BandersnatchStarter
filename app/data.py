from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

load_dotenv()


class Database:

    def __init__(self):
        mongo_url = getenv("DB_URL")

        print(f"DEBUG DB_URL: '{mongo_url}'")  # <-- add this line
        if not mongo_url:
            raise RuntimeError("DB_URL is missing or empty!")

        self.client = MongoClient(mongo_url, tlsCAFile=where())
        self.db = self.client['labs_database']
        self.collection = self.db['monsters']

    def seed(self, amount):
        '''Generates a list of monsters according to the amount
        ordered when the method is executed. That list will be
        inserted into MongoDB. Returns the inserted ids.'''

        monster_list = []

        for _ in range(amount):
            monster = Monster()
            monster_dict = monster.to_dict()
            monster_list.append(monster_dict)

        result = self.collection.insert_many(monster_list)
        return result.inserted_ids

    def reset(self):
        '''Deletes all the documents from the Monsters collection and
        returns the count of deleted docs.'''

        result = self.collection.delete_many({})
        return result.deleted_count

    def count(self) -> int:
        '''Counts all the documents in the Monsters collection
        and returns an integer with that count.'''

        result = self.collection.count_documents({})
        return result

    def dataframe(self) -> DataFrame:
        '''Converts the objects in the database into dicts and returns
         all the info as a Pandas DataFrame.'''

        all_docs = list(self.collection.find())

        for doc in all_docs:
            doc["_id"] = str(doc["_id"])

        result = DataFrame(all_docs)

        return result

    def html_table(self) -> str | None:
        '''Returns an HTML representation of the DataFrame - or None
        if the collection is empty.'''

        df = self.dataframe()

        if df.empty:
            return None

        return df.to_html(index=False,
                          border=0,
                          classes='table table-striped',
                          justify='center')
