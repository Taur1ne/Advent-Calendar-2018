import pprint

def main():
	filename = 'day3_input.txt'
	# filename = 'test1.txt'
	x = 1000
	y= 1000
	
	grid = initialize_grid(x,y)
	items = []
	with open(filename) as f:
		for line in f:
			item = decipher(line.strip('\n'))
			grid = add_to_grid(grid, item)
			items.append(item)
	
	for item_x in items:
		if does_item_overlap(grid, item_x):
			print('Claim ID: ' + str(item_x['claim_id']) + ' does not overlap') 
			exit(0)
	print('Could not identify claim ID')
	
	
def does_item_overlap(grid, item):
	x_start = item['x']
	y_start = item['y']
	height = item['height']
	width = item['width']
	sqft_expected = height * width
	sum = 0
	
	for h in range(0, height):
		new_y = y_start + h
		for w in range(0, width):
			new_x = x_start + w
			cell_value = grid[new_y][new_x]
			claim_id = str(item['claim_id'])
			print('cell_value: ' + cell_value)
			print('Claim ID: ' + claim_id)
			if  cell_value == claim_id:
				sum += 1
	
	print('Claim ID: ' + str(item['claim_id']) + ' Expected Sqft: ' \
		 + str(sqft_expected) + ' Sum: ' + str(sum))
	return sum == height * width

	
def get_overclaimed(twod_list, x, y):
	sum = 0
	for  cur_x in range(0, x):
		for cur_y in range(0, y):
			if twod_list[cur_x][cur_y] == 'x':
				sum += 1
	return sum
			
def initialize_grid(x, y):
	twod_list = []
	for i in range(0,x):
		new = []
		for j in range(0,y):
			new.append('.')
		twod_list.append(new)
	return twod_list

def add_to_grid(grid, item):
	x_start = item['x']
	y_start = item['y']
	for height in range(0, item['height']):
		for width in range(0, item['width']):
			new_x = x_start + width
			new_y = y_start + height
			
			cur_cell = grid[new_y][new_x]
			new_cell = '.'
			if cur_cell == '.':
				new_cell = str(item['claim_id'])
			else:
				new_cell = 'x'
			grid[new_y][new_x] = new_cell
	return grid
	
	
def decipher(input):
	input_list = input.split(' ')
	item = {}
	# Remove the # from the front
	item['claim_id'] = int(input_list[0][1:])
	
	# Should return x,y:
	coords = input_list[2].split(',')
	item['x'] = int(coords[0])
	# [-1] removes the : 
	item['y'] = int(coords[1][0:-1])
	
	width,height = input_list[3].split('x')
	item['width'] = int(width)
	item['height'] = int(height)
	
	return item

		
if __name__ == '__main__':
	main()