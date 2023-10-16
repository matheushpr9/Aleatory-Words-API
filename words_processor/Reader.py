from pdfquery import PDFQuery
import os

class Reader:

    def get_words_of_a_pdf(self,path: str):

        files = os.listdir(path)
        print(files)

        allWords = []

        for file in files:
        
            pdf = PDFQuery(path+file)
            pdf.load()

            text_elements = pdf.pq('LTTextLineHorizontal')

            words = [t.text for t in text_elements]
            
        allWords += words

        return allWords