import pprint

def main():
	filename = 'day2_input.txt'
	# filename = 'test1.txt'
	
	lines = []
	with open(filename) as f:
		for line in f:
			lines.append(line.strip('\n'))
	pprint.pprint(lines)
	x = 0		
	while x < len(lines):
		for y in range(x, len(lines)):
			line1 = lines[x]
			line2 = lines[y]
			print('Comparing:\n ' + line1 + '\n' + line2)
			if sum([int(i!=j) for i,j in zip(line1,line2)]) == 1:
				print('Line 1: ' + lines[x])
				print('LIne 2: ' + lines[y])
				exit(0)
		x += 1
	print('Didn\'t figure it out')
		


		
if __name__ == '__main__':
	main()