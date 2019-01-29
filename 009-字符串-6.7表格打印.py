tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
	len_col = len(tableData)
	colWidths = [0] * len_col
	
	for i in range(len_col):
		for tempLines in tableData[i]:
			if len(tempLines) > colWidths[i]:
				colWidths[i] = len(tempLines)

	
	for j in range(len(tableData[i])):
		for i in range(len_col):
			if i==0:
				print(tableData[i][j].rjust(colWidths[i]) + ' ', end='')
			else:
				print(tableData[i][j].ljust(colWidths[i]) + ' ', end='')
		print('\n',end ='')

	

'''
	maxLine = 0
	for i in range(len_col):
		if colWidths[i] > maxLine:
			maxLine = colWidths[i]
	
	return maxLine
'''

printTable(tableData)
