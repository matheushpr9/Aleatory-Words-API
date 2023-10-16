class Wordsmith:
    def treat_word(self, word: str)-> str:
        return ''.join([letter for letter in word  if letter.isalnum() and not letter.isdecimal()])