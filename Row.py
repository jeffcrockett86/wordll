class Row:
    def __init__(self, word, parent):
        self.word = word
        self.parent = parent
        self.cells = []
        self.html = '<tr> </tr>'
