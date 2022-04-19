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
    This program produces the hangman game with picture, but just for 7 life.
    """
    life = 7
    answer = random_word()
    guess = ''
    for i in range(len(answer)):
        guess += '-'
    while True:
        print('The word looks like: ' + guess)
        print('You have ' + str(life) + ' guesses left.')
        hangman_picture(life)
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
                hangman_picture(life)
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


def hangman_picture(life):
    """
    This function produces the hangman picture based on life in the following order:
    Head, left hand, body, right hand, left leg, right leg, death
    """
    for i in range(7):
        print('===', end='')
    print('')
    for i in range(14):
        print('||', end='')
        rope(i)
        if life != 0:
            if life <= 6:
                head(i)
            if life <= 5:
                left_hand(i)
            if life <= 4:
                body(i)
            if life <= 3:
                right_hand(i)
            if life <= 2:
                left_leg(i)
            if life == 1:
                right_leg(i)
        else:
            death(i)
        print('')


def rope(x):
    """
    This function produces the rope picture with input x as the location point
    """
    if 0 <= x <= 2:
        for i in range(18):
            print(' ', end='')
        print('|', end='')


def head(x):
    """
    This function produces the hangman head with input x as the location point
    """
    if x == 3:
        for i in range(15):
            print(' ', end='')
        for j in range(3):
            print('__', end='')
    if x == 4:
        for i in range(14):
            print(' ', end='')
        print('/', end='')
        for j in range(6):
            print(' ', end='')
        print('\\', end='')
    if x == 5:
        for i in range(14):
            print(' ', end='')
        print('\\', end='')
        for j in range(6):
            print('_', end='')
        print('/', end='')


def body(x):
    """
    This function produces the hangman body with input x as the location point
    """
    if x == 6 or 8 <= x <= 9:
        for i in range(18):
            print(' ', end='')
        print('|', end='')
    if x == 7:
        print('|', end='')


def left_hand(x):
    """
    This function produces the hangman left hand with input x as the location point
    """
    if x == 7:
        for i in range(13):
            print(' ', end='')
        for j in range(5):
            print('_', end='')


def right_hand(x):
    """
    This function produces the hangman right hand with input x as the location point
    """
    if x == 7:
        for i in range(5):
            print('_', end='')


def left_leg(x):
    """
    This function produces the hangman left leg with input x as the location point
    """
    if 10 <= x <= 11:
        for i in range(27 - x):
            print(' ', end='')
        print('/', end='')


def right_leg(x):
    """
    This function produces the hangman right leg with input x as the location point
    """
    if 10 <= x <= 11:
        for i in range(x * 2 - 19):
            print(' ', end='')
        print('\\', end='')


def death(x):
    """
    This function produces the hangman death picture with input x as the location point
    """
    if x == 3:
        for i in range(15):
            print(' ', end='')
        for j in range(3):
            print('__', end='')
    if x == 4:
        for i in range(14):
            print(' ', end='')
        print('/', end='')
        print(' x  x ', end='')
        print('\\', end='')
    if x == 5:
        for i in range(14):
            print(' ', end='')
        print('\\', end='')
        for j in range(6):
            print('_', end='')
        print('/', end='')
    left_hand(x)
    body(x)
    right_hand(x)
    left_leg(x)
    right_leg(x)


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
