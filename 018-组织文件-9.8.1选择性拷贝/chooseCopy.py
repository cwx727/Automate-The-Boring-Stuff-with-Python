import os, shutil

for folderName, subfolders, filenames in os.walk('./file/'):
	for filename in filenames:
		if filename.endswith('.svg') or filename.endswith('.jpg'):
			file_dir = os.path.join(folderName, filename)
			if os.path.exists('./file_copy/'):   #判断文件夹是否存在，不存在创建
				shutil.copy(file_dir, './file_copy/')
			else:
				os.makedirs('./file_copy/')
				shutil.copy(file_dir, './file_copy/')




