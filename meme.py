class Table:
    def __init__(self, name):
        self.name = name
        self.rows = []
class Row:
    def __init__(self, parent):
        self.parent = parent
        self.name = ''
        self.cells = []

class Col:
    def __init__(self, parent):
        self.parent = parent
        self.name = ''
        self.cells = []

class Cell:
    def __init__(self, parent):
        self.parent = parent
        self.name = ''
        self.tables = []
