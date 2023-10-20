from words_processor.Reader import Reader
import os
from Wordsmith import Wordsmith
from database.Connector import Connector

reader_controller = Reader()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

phrase = reader_controller.get_words_of_a_pdf(BASE_DIR+"/books/portuguese/")

words = []

for word in phrase:
    words += word.split(" ")
wordsmithController = Wordsmith()

wordsTreated = [ wordsmithController.treat_word(word) for word in words]

connector = Connector("matheushpr9", "bZw23JHQYa9OrXLm")

for wordTreated in wordsTreated:
    if len(wordTreated) >=5:
        connector.add_new_word("portuguese", wordTreated)