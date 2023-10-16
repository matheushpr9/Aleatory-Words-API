import pymongo

class Connector:
    
    def __init__(self, username, password):

        print("[Database] Setting the connection...")

        self.connection = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ohgpvy0.mongodb.net/?retryWrites=true&w=majority")
        self.database = self.connection["words-api"]

        print("[Database] Connection successfully established with words-api Database!")
    
    def create_new_collection(self, name:str, data: dict):
        print("[Database] Creating a new collection: "+ name)

        new_collection = self.database[name]

        r = new_collection.insert_one(data)

        print(f"[Database] New Collection {name} successfully created!")

    def set_word(self,word: str, collection: str):
        return {

            "_id":self.get_collection_length(collection),
            "lower": word.lower(),
            "upper": word.upper(),
            "capitalize": word.capitalize(),
            "len": len(word),
                
            }
    

    def add_new_word(self, collection: str, word: str):
        data = self.set_word(word, collection)
        if collection not in self.database.list_collection_names():
            print(f"[Database] Collection {collection} not found.")
            self.create_new_collection(collection,data)

        else:
            if not self.word_exists(data, collection):
                print(f"[Database] adding a new word: {word}!")
                self.database[collection].insert_one(data)
                print(f"[Database] New word {word} added!")
            else:
                print(f"[Database] The word {word} already exist in database!")

    def word_exists(self, data: str, collection: str):
        collection_to_query = self.database[collection]
        query = collection_to_query.find(data)
        

        for x in query:
            return True
        
        return False

    def get_collection_length(self, collection: str) -> int:
        return len(list(self.database[collection].find()))
    
    def get_item_by_id(self, collection: str, id:int) -> dict:
        return list(self.database[collection].find({"_id":id}))[0]
