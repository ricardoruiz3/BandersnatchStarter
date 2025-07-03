from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self):
        load_dotenv()
        mongo_url = getenv("DB_URL")

        self.client = MongoClient(mongo_url, tlsCAFile=where())

        self.db = self.client['labs_database']
        self.collection = self.db['monsters']

    def seed(self, amount):
        '''This function will generate a list of monsters according to the
        amount # that is ordered when the method is executed. That list will
        then be inserted into MongoDB.'''

        monster_list = []

        for _ in range(amount):
            monster = Monster()
            monster_dict = monster.to_dict()
            monster_list.append(monster_dict)

        result = self.collection.insert_many(monster_list)
        return result.inserted_ids

    def reset(self):
        result 

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass


client = MongoClient("mongodb://localhost:27017/")
db = client["nombre_base"]
collection = db["nombre_coleccion"]
