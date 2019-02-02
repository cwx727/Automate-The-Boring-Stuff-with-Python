import os,shutil

filenames = []
file_dir ='./file/'
for filename in os.listdir(file_dir):
	if filename.startswith('spam'):
		filenames.append(filename)

filenames.sort()

i=1
for filename in filenames:
	move_filename = 'spam00' + str(i) + '.txt'
	move_filename_dir = file_dir + move_filename
	if filename == move_filename:
		i +=1
		continue
	else:
		#print(file_dir+filename,move_filename_dir)
		shutil.move(file_dir+filename, move_filename_dir)
		i +=1

		

		
'''
for folderName, subfolders, filenames in os.walk('./'):
	for filename in filenames:
		file_dir = os.path.join(folderName, filename)
		if os.path.getsize(file_dir) > 1000: 
			print(file_dir)
'''



