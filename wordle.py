import random
import sys


f = open('wordleAlpha.txt', 'r')
words = f.read().split('\n')[:-1]
# answer = words[random.randint(0, len(words))]
answer = 'sever'
print('Answer is', answer, '\n\n')


def wordle(guesses, answer, words=words, allowed=[], word_length=5, guess_num=0):
    if len(guesses)==0:
        return 'That\'s all folks'
    if guess_num == 0:
        print('Welcome to Word\'ll!\n')
    if guess_num > 0:
        print(words)
    print(f'{len(words)} words are left')
    if len(guesses) > 0:
        guess =guesses[0]
        print('Guess is', guess)

    for i in range(word_length):
        if guess[i] == answer[i]:
            # words = list(filter(lambda word: word[i] == answer[i] , words))
            words = [word for word in words if word[i] == answer[i]]
            allowed.append(guess[i])
            print(guess[i], 'is green')
        elif guess[i] in answer and guess[i] != answer[i]:
            # words = list(filter(lambda word: word[i] in answer and word[i] != answer[i] , words))
            words = [word for word in words if guess[i] in word and word[i] != guess[i]]
            print(guess[i], 'is yellow')
            allowed.append(guess[i])
        elif guess[i] not in answer:
                # words = list(filter(lambda word: guess[i] not in word, words))
                words = [word for word in words if guess[i] not in word]

    # if len(words) > 0:
        # print(f'\nThere are {len(words)} words left\n')
    guesses = guesses[1:]
    guess_num += 1
    return wordle(guesses, answer, words=words, allowed=allowed, guess_num=guess_num)

print(wordle(sys.argv[1:], answer))
