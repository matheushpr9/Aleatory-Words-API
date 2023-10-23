from dotenv import load_dotenv
import os
from app.database.Connector import Connector
from app.classes.Word import Word
from app.controllers.CollectionController import CollectionController
load_dotenv()

class WordController:
    def __init__(self) -> None:
        print("[WordController] Initializing a new instance!")
        connector = Connector(os.getenv('DATABASE_USER'),  os.getenv('DATABASE_PASSWORD'))
        self.connector =  connector
        self.database = connector.get_database()
        self.collectionController = CollectionController()
        print("[WordController] New instance constructed!")
    
    def word_exists(self, data: str, collection: str) -> bool:
        collection_to_query = self.database[collection]
        print(data)
        query = collection_to_query.find({"word":data["word"]})
        
        for x in query:
            return True
        
        return False

    def add_new_word(self, word: str, collection: str) -> None:
        new_word = Word(word)
        data = new_word.prepare_word_to_database(collection)

        if not self.collectionController.collection_exists(collection):
            print(f"[Database] Collection {collection} not found.")
            self.collectionController.create_new_collection(collection,data)

        else:
            if not self.word_exists(data, collection):
                print(f"[Database] adding a new word: {word}!")
                self.connector.new_insertion(data, collection)
                print(f"[Database] New word {word} added!")
            else:
                print(f"[Database] The word {word} already exist in database!")

    def get_word_by_id(self, collection: str, id:int) -> dict:
        return list(self.database[collection].find({"_id":id}))[0]

    def get_all_words_attributes(self, data: dict):
        word = Word(data["word"])

        return{
            "_id": data["_id"],
            "lower": word.get_lower_word(),
            "upper": word.get_upper_word(),
            "capitalize":word.get_capitalize_word(),
            "length": word.get_word_length()
        }