import re
import itertools

def solve(puzzle):
	words = re.findall('[A-Z]+', puzzle.upper())
	# print(words)
	unique_characters = set(''.join(words))
	# print(unique_characters)
	assert len(unique_characters) <= 10, 'Too many letters'
	first_letters = {word[0] for word in words}
	# print(first_letters)
	n = len(first_letters)
	sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
	# print(sorted_characters)
	characters = tuple(ord(c) for c in sorted_characters)
	# print(characters)
	digits = tuple(ord(c) for c in '0123456789')
	# print(digits)
	zero = digits[0]
	# print(zero,n)
	for guess in itertools.permutations(digits, len(characters)):
		# print(guess[:n])
		if zero not in guess[:n]:
			equation = puzzle.translate(dict(zip(characters, guess)))
			# print('\n',equation,'\n')
			if eval(equation):
				return equation

if __name__ == '__main__':
	import sys
	for puzzle in sys.argv[1:]:
		print(puzzle)
		solution = solve(puzzle)
		if solution:
			print(solution)