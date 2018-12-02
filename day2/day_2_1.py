import pprint
def main():
	filename = 'day2_input.txt'
	two_letter_checksum = 0
	three_letter_checksum = 0

	with open(filename) as f:
		for line in f:
			letter_bools = get_two_or_three_letter_counts(line.strip('\n'))
			print('line: ' + line)
			pprint.pprint(letter_bools)
			two_letter_checksum += letter_bools[0]
			three_letter_checksum += letter_bools[1]
		checksum = two_letter_checksum * three_letter_checksum
		print('Checksum: ' + str(checksum))

def get_two_or_three_letter_counts(word):
	letter_map = {}
	uniq_letters = []
	has_two_letter_chars = False
	has_three_letter_chars = False
	for c in word:
		try:
			letter_map[c] += 1
		except KeyError:
			letter_map[c] = 1
			uniq_letters.append(c)
	pprint.pprint(letter_map)
	pprint.pprint(uniq_letters)
	for letter in uniq_letters:
		try:
			if letter_map[letter] == 2:
				has_two_letter_chars = True
			elif letter_map[letter] == 3:
				has_three_letter_chars = True
			if has_three_letter_chars and has_two_letter_chars:
				return [has_two_letter_chars, has_three_letter_chars]
		except KeyError:
			print('Letter' + letter + ' did not show up in letter_map')
	return [has_two_letter_chars, has_three_letter_chars]







if __name__ == '__main__':
	main()