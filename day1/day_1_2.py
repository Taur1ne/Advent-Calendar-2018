import pprint



def main():
	frequency = 0
	val_map = {}
	val_map[frequency] = 1
	gains(val_map, './day1_input.txt')
	#gains(val_map, './test1.txt')

	
def gains(val_map, filename):
	frequency = 0
	counter = 1
	i = 0
	while True:
		with open(filename) as f:
				for line in f:
					print('Line number: ' + str(counter) + ' Line: ' + line)
					frequency += int(line)
					counter+=1
					try:
						val_map[frequency] +=1
						if val_map[frequency] == 2:
							print('Repeat frequency found: ' + str(frequency))
							exit(0)
					except KeyError:
						val_map[frequency] = 1
				print(frequency)
				print(counter)

				#pprint.pprint(val_map)
		i += 1
	
	
if __name__ == '__main__':
	main()