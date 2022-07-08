

class Row:
    def __init__(self, word):
        self.word = word
        self.cells = []

    def print(self):
        print(' '.join([cell.letter for cell in self.cells]))
