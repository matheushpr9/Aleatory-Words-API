from typing import Union
from fastapi import FastAPI
from app.controllers.WordController import WordController
from app.controllers.CollectionController import CollectionController
from random import randrange

app = FastAPI()

@app.get("/")
def read_root():
    return{
        "Hello": "World",
        "message": "Welcome to Aleatory Words API! Take a look on the documentation :)"
        }

@app.get("/word/{language}/")
def get_aleatory(language:str, q: str = None):
    word_controller = WordController()
    collection_controller = CollectionController()

    word = word_controller.get_word_by_id(language, randrange(collection_controller.get_collection_length(language)))
    data = word_controller.get_all_words_attributes(word)

    if q:
        return data[q.lower()] if q.lower() in data else data
    
    return data
