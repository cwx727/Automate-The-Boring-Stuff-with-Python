import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
		
	print('Removing header from ' + csvFilename + '...')
	
	#读取csv内容，去除第一行
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue
		csvRows.append(row)
	
	
		csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
		csvWriter = csv.writer(csvFileObj)
		for row in csvRows:
			csvWriter.writerow(row)
	
	csvFileObj.close()
