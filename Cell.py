class Cell:
    def __init__(self, letter, parent):
        self.parent = parent
        self.letter = letter
        self.tables = []
        self.html = '<td> </td>'
        self.is_green = False
        self.is_yellow = False
        self.is_gray = False