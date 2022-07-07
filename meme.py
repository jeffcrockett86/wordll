import re
from Grid import Grid
from Row import Row
from Col import Col
from Cell import Cell
from termcolor import colored

#i think that I shall never see a poem lovely as a tree
f = open('wordleAlpha.txt', 'r')
words = f.read().split('\n')[:-1]

# answer = words[random.randint(0, len(words))]
answer = 'sever'
print('Answer is', answer, '\n\n')


def make_grid():
    g = Grid('Wordle')
    g.rows = [Row(f'Guess {i}', g) for i in range(6)]
    for row in g.rows:
        row.cells = [Cell(f'Letter {i}', parent=row) for i in range(5)]
    return g

def valid(guess):
    return re.match(r"^[a-z]{5}$", guess.lower())

# print([row.name for row in m.rows])
# print([cell for row in m.rows for cell in row.cells])
answer = 'stack'





    #trim the name of the file off sys.argv




def analyze(cell, answer, index, words=words):
    if cell.letter == answer[index]:
        # words = list(filter(lambda word: word[i] == answer[i] , words))
        words = [word for word in words if word[i] == answer[i]]
        # allowed.append(guess[i])
        cell.is_green = True
        print(guess[i], 'is green')
        cell.letter = colored(cell.letter, 'green')
    elif cell.letter in answer and cell.letter != answer[i]:
        # words = list(filter(lambda word: word[i] in answer and word[i] != answer[i] , words))
        words = [word for word in words if cell.letter in word and word[i] != cell.letter]
        print(cell.letter, 'is yellow')
        cell.is_yellow = True
        cell.letter = colored(cell.letter, 'yellow')

        # allowed.append(guess[i])
    elif cell.letter not in answer:
            # words = list(filter(lambda word: guess[i] not in word, words))
            words = [word for word in words if guess[i] not in word]
            cell.is_gray = True
            cell.letter = colored(cell.letter, 'gray')


#so far should put the first guess in the grid. colors haven't been added yet
def play(words=words):
    word_length = 5
    guess_num = 0
    grid = make_grid()
    guess = input(f'Guess {guess_num  + 1}')
    if valid(guess):
        while guess_num < 6:
            for i in range(word_length):
                grid.rows[guess_num].cells[i].letter = guess[i]
                analyze(grid.rows[guess_num].cells[i], i)
            guess_num += 1

    return grid
