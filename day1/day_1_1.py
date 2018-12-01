value = 0
counter = 1
with open('./day1_input.txt') as f:
	for line in f:
		print('Line number: ' + str(counter) + ' Line: ' + line)
		value += int(line)
		counter+=1
print(value)
print(counter)