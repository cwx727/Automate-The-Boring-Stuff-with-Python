import PyPDF2

with open('dictionary.txt') as obj_f:
	psws = obj_f.readlines()


pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

	
for psw in psws:
	if pdfReader.decrypt(psw.rstrip()) == 0 and pdfReader.decrypt(psw.rstrip().lower()) == 0:
		continue
	elif pdfReader.decrypt(psw.rstrip().lower()) == 1:
		print(psw.rstrip().lower())
		break
	elif pdfReader.decrypt(psw.rstrip()) == 1:
		print(psw.rstrip())
		break
	else:
		print('all passwords is not correct.')

		
	
