import openpyxl,os

#创建一个新的excel

filedir = './file/'
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()

i=1

#取到某个文件夹下完整的文件路径
for filename in os.listdir(filedir):
	filedirname = filedir + filename
	#打开文件逐行读取
	with open(filedirname) as obj_f:
		lines = obj_f.readlines()
		j=1
		#值写入对应单元格
		for line in lines:
			sheet.cell(row=j,column=i).value = line.strip()
			j += 1
		i += 1
	
wb.save('txttoxlsx.xlsx')
		






