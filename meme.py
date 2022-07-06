class Table:
    def __init__(self, name):
        self.name = name
        self.rows = []

class Row:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.cells = []

class Col:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.cells = []

class Cell:
    def __init__(self, name, parent):
        self.parent = parent
        self.name = name
        self.tables = []

def make_table():
    t = Table('Wordle')
    t.rows = [Row(f'Guess {i}', t) for i in range(6)]
    for row in t.rows:
        row.cells = [Cell(f'Letter {i}', parent=row) for i in range(5)]
    return t
# class M:
#     def __init__(self, name):
#         self.name = name
#         self._E = []
# class _E:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.E = []

# class _M:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.E = []

# class E:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.M = []

# class A:
#     def __init__(self, name):
#         self.name = name
#         self.C = []
# class C:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.G = []

# class T:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.G = []

# class G:
#     def __init__(self, parent):
#         self.parent = parent
#         self.name = ''
#         self.A = []
