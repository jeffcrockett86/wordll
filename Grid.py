from Row import Row
from Cell import Cell

class Grid:
    def __init__(self, name):
        self.name = name
        self.rows = []

    def add_row(self, word):
        self.rows.append(Row(word, self))
        self.rows[-1].cells = [Cell(letter) for letter in word]

    @property
    def cells(self):
        return [cell for row in self.rows for cell in row.cells]
