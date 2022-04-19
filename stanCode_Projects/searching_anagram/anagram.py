"""
File: anagram_for_speed_test.py
Name: Jerry Ju
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
DICT = []                     # The dictionary to search the anagrams


def main():
    """
    This function asks user to input a word, and finds all the anagrams of the word
    """
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        if word == EXIT:
            break
        else:
            find_anagrams(word)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: list, the dictionary to find the anagrams
    """
    with open(FILE, 'r') as f:
        for line in f:
            DICT.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, the string needed to find anagrams
    This function will print all of the anagrams of the input word
    """
    anagrams = []
    print('Searching...')
    find_anagrams_helper(s, len(s), [], anagrams)
    print(len(anagrams), 'anagrams:', anagrams)


def find_anagrams_helper(s, ans_len, order, anagrams):
    """
    :param s: str, the string needed to find anagrams
    :param ans_len: int, the length of the answer
    :param order: list, the different order of the character in the input word in order to compose a new word
    :param anagrams: list, all of the anagrams of the input word
    This function will print all of the anagrams of the input word
    """
    current_s = ''
    # early stopping
    if len(order) == ans_len//2:
        for num in order:
            current_s += s[num]
        if not has_prefix(current_s):
            return

    # base case
    if len(order) == ans_len:
        for num in order:
            current_s += s[num]
        if current_s in DICT and current_s not in anagrams:
            print('Found:', current_s)
            print('Searching...')
            anagrams.append(current_s)

    # recursion
    else:
        for i in range(ans_len):
            if i not in order:
                # choose
                order.append(i)
                # explore
                find_anagrams_helper(s, ans_len, order, anagrams)
                # un-choose
                order.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, the input string
    :return: Boolean, if any word in the dictionary starts with the input string
    """
    for word in DICT:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
