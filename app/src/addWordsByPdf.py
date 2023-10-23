from words_processor.Reader import Reader
import os
from app.controllers.WordController import WordController 
from definitions import ROOT_DIR

reader_controller = Reader()
word_controller = WordController()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

phrase = reader_controller.get_words_of_a_pdf(ROOT_DIR+"/pdfs/portuguese/")

words = []

for word in phrase:
    words += word.split(" ")

wordsTreated = [ reader_controller.treat_word(word) for word in     words]

for wordTreated in wordsTreated:
    if len(wordTreated) >=5:
        word_controller.add_new_word(wordTreated, "portuguese")