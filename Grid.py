from Row import Row
from Cell import Cell

class Grid:
    def __init__(self, name):
        self.name = name
        self.rows = []
        self.html = '<table> </table>'
        self.val = None


    # def p(self):
    #     print(cell.letter for row in self.rows for cell in row.cells)

    def add_row(self, word):
        self.rows.append(Row(word, self))
        self.rows[-1].cells = [Cell(letter, self.rows[-1]) for letter in word]

    @property
    def cells(self):
        return [cell for row in self.rows for cell in row.cells]
