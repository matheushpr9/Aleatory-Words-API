from dotenv import load_dotenv
import os
from ..database.Connector import Connector
from ..classes.Collection import Collection

load_dotenv()

class CollectionController:
    def __init__(self) -> None:
        self.connection = Connector(os.getenv('DATABASE_USER'),  os.getenv('DATABASE_PASSWORD'))

    def collection_exists(self, collection: str):
        return True if collection not in self.connection.database.list_collection_names() else False

    def create_new_collection(self, collection: str, word: str):
        print("[Collection Controller] Creating a new collection: "+ collection)

        new_collection = self.database[collection]

        r = new_collection.insert_one(word)

        print(f"[Collection Controller] New Collection {word} successfully created!")

    
    def get_collection_length(self, collection: str) -> int:
        return len(list(self.database[collection].find()))
    
