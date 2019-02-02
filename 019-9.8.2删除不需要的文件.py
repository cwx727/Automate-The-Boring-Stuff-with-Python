import os

for folderName, subfolders, filenames in os.walk('./'):
	for filename in filenames:
		file_dir = os.path.join(folderName, filename)
		if os.path.getsize(file_dir) > 1000: 
			print(file_dir)




