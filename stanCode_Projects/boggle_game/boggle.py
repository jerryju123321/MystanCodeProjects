"""
File: boggle.py
Name: Jerry Ju
----------------------------------------
This program simulates the famous boggle game. It will ask the user input 16 characters to form a 4x4 square,
and give the linked words based on the characters
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program simulates the famous boggle game
	"""
	dictionary = read_dictionary()
	rows = {}
	rows[0] = input('1 row of letters: ').split()
	if is_right_form(rows[0]):
		rows[1] = input('2 row of letters: ').split()
		if is_right_form(rows[1]):
			rows[2] = input('3 row of letters: ').split()
			if is_right_form(rows[2]):
				rows[3] = input('4 row of letters: ').split()
				if is_right_form(rows[3]):
					start = time.time()
					check_boggles(rows, dictionary)
					end = time.time()
					print('----------------------------------')
					print(f'The speed of your boggle algorithm: {end - start} seconds.')


def check_boggles(rows, dictionary):
	"""
	:param rows: Dict, the rows contain all the input characters
	:param dictionary: List, the dictionary to search the words
	This function will check the linked words from the input characters based on the dictionary
	"""
	words = []  # List contains all the found word
	for i in range(4):
		for j in range(4):
			rows_order = [(i, j)]  # the first order
			check_boggles_helper(rows, rows_order, i, j, words, dictionary)
	print(f'There are {len(words)} words in total.')


def check_boggles_helper(rows, rows_order, x_position, y_position, words, dictionary):
	"""
	:param rows: Dict, the rows contain all the input characters
	:param rows_order: List, the order that composed the word based on rows
	:param x_position: int, current x position to find the neighbor
	:param y_position: int, current y position to find the neighbor
	:param words: List, contains all the found word
	:param dictionary: List, the dictionary to search the words
	"""
	current_s = ''
	for t in rows_order:
		current_s += rows[t[0]][t[1]]
		current_s = current_s.lower()

	# early stopping
	if len(current_s) >= 2:
		if not has_prefix(current_s, dictionary):
			return

	# base case
	if len(current_s) >= 4:
		if current_s in dictionary and current_s not in words:
			if len(rows_order) >= 4:
				words.append(current_s)
				print(f'Found: "{current_s}"')

	# recursion:
	if len(current_s) <= 5:
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				if 0 <= x_position + i <= 3 and 0 <= y_position + j <= 3:
					if (x_position + i, y_position + j) not in rows_order:
						# choose
						rows_order.append((x_position + i, y_position + j))
						# explore neighbor
						check_boggles_helper(rows, rows_order, x_position+i, y_position+j, words, dictionary)
						# un-explore
						rows_order.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())
	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (List) the dictionary to find the words
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


def is_right_form(row):
	"""
	:param row: List, the input row
	:return: Bool, whether the input row is right form
	"""
	for ch in row:
		if not ch.isalpha() or len(ch) != 1:
			print('Illegal input')
			return False
	if len(row) != 4:
		print('Illegal input')
		return False
	return True


if __name__ == '__main__':
	main()
