import re
import os

file_Res = []

re_text = str(input('please input the words you want to find:'))

#找到文件夹所在目录的所有的txt文件
for folderName, subfolders, filenames in os.walk(os.getcwd()):
	for filename in filenames:
		if re.compile(r'.*\.txt').search(filename) != None:
			file_Res.append(filename)

#遍历所有的txt文件，读取内容，并re查找内容，输出
for file_Re in file_Res:
	file_Re_dir = ('./'+file_Re)
	#print(file_Re_dir)
	with open(file_Re_dir) as f_obj:
		file_texts = f_obj.readlines()
	#print(file_text)
	for file_text in file_texts:
		fileRefind = re.compile(r'(.*)%s(.*)'%re_text).search(file_text)
		if fileRefind != None:
			print("filename:" + file_Re + "--------find text:" + fileRefind.group())
