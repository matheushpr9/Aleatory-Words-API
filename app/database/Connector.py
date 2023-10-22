import pymongo

class Connector:
    
    def __init__(self, username, password):

        print("[Database] Setting the connection...")

        self.connection = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ohgpvy0.mongodb.net/?retryWrites=true&w=majority")
        self.database = self.connection["words-api"]

        print("[Database] Connection successfully established with words-api Database!")