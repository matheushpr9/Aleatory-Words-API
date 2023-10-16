from typing import Union
from fastapi import FastAPI
from database.Connector import Connector
from random import randrange

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/word/{language}")
def get_aleatory(language:str):
    connector = Connector("matheushpr9", "bZw23JHQYa9OrXLm")
    word = connector.get_item_by_id(language, randrange(connector.get_collection_length(language)))
    return word

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return({"item_id": item_id, "q": q})