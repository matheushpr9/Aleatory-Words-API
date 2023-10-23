from ..controllers.CollectionController import CollectionController
class Word:
    def __init__(self, word: str) -> None:
        self.word = word

    def get_lower_word(self) -> str:
        return self.word.lower()
    
    def get_upper_word(self) -> str:
        return self.word.upper()
    
    def get_capitalize_word(self) -> str:
        return self.word.capitalize()
    
    def get_word_length(self) -> int:
        return len(self.word)

    def prepare_word_to_database(self, collection: str):
        collectionController = CollectionController()
        return {
            "_id": collectionController.get_collection_length(collection),
            "word": self.get_lower_word()
            }
    