import csv, os, openpyxl

os.makedirs('CSVs', exist_ok=True)

for excelFile in os.listdir('./excelSpreadsheets/'):
	# Skip non-xlsx files, load the workbook object.
	if not excelFile.endswith('.xlsx'):
		continue
	wb = openpyxl.load_workbook(os.path.join('excelSpreadsheets',excelFile))
	
	for sheetName in wb.get_sheet_names():
		# Loop through every sheet in the workbook.
		sheet = wb.get_sheet_by_name(sheetName)
		
		# Create the CSV filename from the Excel filename and sheet title.
		csvFilename = excelFile[:-5] + '_' + sheetName + '.csv'
		csvFile = os.path.join('CSVs',csvFilename)
		#print(csvFile)
		
		# Create the csv.writer object for this CSV file.
		csvFile = open(csvFile, 'w', newline='')
		writerObj = csv.writer(csvFile)
		
		# Loop through every row in the sheet.
		for rowNum in range(1, sheet.max_row + 1):
			rowData = [] # append each cell to this list
			# Loop through each cell in the row.
			for colNum in range(1, sheet.max_column + 1):
				# Append each cell's data to rowData.
				rowData.append(sheet.cell(row=rowNum,column=colNum).value)

			# Write the rowData list to the CSV file.
			writerObj.writerow(rowData)
			
		#csvFile.close()
		csvFile.close()
