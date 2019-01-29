def list_transfer_grid(lists):
	len_y = len(lists)
	len_x = len(lists[0])

	for temp_x in range(len_x):
		for temp_y in range(len_y):
			print(lists[temp_y][temp_x], end = '')
		print('\n',end = '')

grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]	

list_transfer_grid(grid)
	

	


	


