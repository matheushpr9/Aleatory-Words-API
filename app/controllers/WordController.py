from dotenv import load_dotenv
import os
from app.database.Connector import Connector
from app.classes.Word import Word
from .CollectionController import CollectionController

load_dotenv()

class WordController:
    def __init__(self) -> None:
        self.connection = Connector(os.getenv('DATABASE_USER'),  os.getenv('DATABASE_PASSWORD'))
    
    def word_exists(self, word: str, collection: str) -> bool:
        collection_to_query = self.connection.database[collection]
        query = collection_to_query.find(word)
        
        for x in query:
            return True
        
        return False

    def add_new_word(self, word: str, collection: str) -> None:
        new_word = Word(word)
        data = new_word.prepare_word_to_database(collection)

        collectionController = CollectionController()
        if not collectionController.collection_exists(collection):
            print(f"[Database] Collection {collection} not found.")
            collectionController.create_new_collection(collection,data)

        else:
            if not self.word_exists(data, collection):
                print(f"[Database] adding a new word: {word}!")
                self.database[collection].insert_one(data)
                print(f"[Database] New word {word} added!")
            else:
                print(f"[Database] The word {word} already exist in database!")

    def get_word_by_id(self, collection: str, id:int) -> dict:
        return list(self.database[collection].find({"_id":id}))[0]

        