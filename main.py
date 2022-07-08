import re
from Grid import Grid
from Row import Row
from Cell import Cell
from termcolor import colored
import random

f = open('wordleAlpha.txt', 'r')
words = f.read().split('\n')[:-1]
answer = words[random.randint(0, len(words))]




def valid(guess):
    return re.match(r"^[a-z]{5}$", guess.lower())


def assign_colors(row, answer, words=words):
    colored_letters = []
    for i in range(5):
        letter = row.cells[i].letter
        if letter == answer[i]:
            # words = list(filter(lambda word: word[i] == answer[i] , words))
            words = [word for word in words if word[i] == answer[i]]
            letter = colored(letter, 'green')
            colored_letters.append(letter)
        elif letter in answer and letter != answer[i]:
            words = [word for word in words if letter in word and word[i] != letter]
            letter = colored(letter, 'yellow')
            colored_letters.append(letter)
        elif letter not in answer:
            words = [word for word in words if letter not in word]
            letter = colored(letter, 'grey')
            colored_letters.append(letter)

            # colored_letters += letter
    return colored_letters

# def assign_colors(row, guess):
#     for i in range(len(guess)):
#         cell = row.cells[i]
#         cell.letter = guess[i]
        # if cell.is_green:
        #     cell.letter = colored(cell.letter, 'green')
        # elif cell.is_yellow:
        #     cell.letter = colored(cell.letter, 'yellow')
        # elif cell.is_grey:
        #     cell.letter = colored(cell.letter, 'grey')


# def display_letters(grid):
#     for row in grid.rows:
#         print([cell for cell in row.cells])

# #so far should put the first guess in the grid. colors haven't been added yet
def play(words=words):
    print('Welcome to Word\'ll!\n\n')
    guess_num = 0
    grid = Grid("Wordle")
    # guess_letters = [cell.letter for cell in grid.rows[-1].cells]
    while guess_num < 6:
        guess = input(f'\nGuess {guess_num  + 1}\n\n')

        if not valid(guess):
            while not valid(guess):
                print('\n\nInvalid guess\n')
                guess = input(f'Guess {guess_num  + 1}\n\n')
        grid.add_row(guess)
        #go through letters of the guess       #5 is the word length
        colored_letters = assign_colors(grid.rows[-1], answer)
        print(' '.join(colored_letters))
        if guess == answer:
            print('\n\nYou win!')
            return
        guess_num += 1
    print(f'\n\nYou lose! The answer was {answer}')

    return grid

play()
