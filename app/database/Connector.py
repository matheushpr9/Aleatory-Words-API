import pymongo

class Connector:
    
    def __init__(self, username, password):

        print("[Connector] Setting the connection...")

        self.connection = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ohgpvy0.mongodb.net/?retryWrites=true&w=majority")
        self.database = self.connection["words-api"]

        print("[Connector] Connection successfully established with words-api Database!")

    def get_connection(self):
        return self.connection
    
    def get_database(self):
        return self.database
    
    def new_insertion(self, data: str, collection: str):
        self.database[collection].insert_one(data)