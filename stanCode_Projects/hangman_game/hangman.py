"""
File: hangman.py
Name: Jerry Ju
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program produces the hangman game
    """
    life = N_TURNS
    answer = random_word()
    guess = ''
    for i in range(len(answer)):
        guess += '-'
    while True:
        print('The word looks like: ' + guess)
        print('You have ' + str(life) + ' guesses left.')
        input_ch = input('Your guess: ')
        if input_ch.isalpha() and len(input_ch) == 1:  # make sure input is a single letter
            input_ch = input_ch.upper()
            if input_ch in answer:
                print('You are correct!')
                guess = change_answer(input_ch, guess, answer)
            else:
                print('There is no ' + input_ch + '\'s in the word.')
                life -= 1
            if guess == answer:  # win condition
                print('You win!!')
                break
            if life == 0:  # lose condition
                print('You are completely hung :(')
                break
        else:
            print('illegal format.')
    print('The word was: ' + answer)


def change_answer(a, b, c):
    """
    :param a: str, the input character to replace the guess answer
    :param b: str, the previous guess answer to be replaced
    :param c: str, the right answer
    :return: str, the new guess answer
    """
    new_guess = ''
    for i in range(len(c)):
        if a == c[i]:
            new_guess += a
        else:
            new_guess += b[i]
    return new_guess


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
