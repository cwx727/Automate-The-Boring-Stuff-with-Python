import PyPDF2,os

passwd = input('please input encrypted password:')
filedirname = ''
for folderName, subfolders, filenames in os.walk('.'):
	#读取文件下所有的pdf文件
	for filename in filenames:
		if filename.endswith('.pdf'):
			filedirname = folderName +'/'+ filename
			
			#复制pdf文件
			pdfFile = open(filedirname, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			pdfWriter = PyPDF2.PdfFileWriter()
			for pageNum in range(pdfReader.numPages):
				pdfWriter.addPage(pdfReader.getPage(pageNum))
			
			#加密文档和存储
			pdfWriter.encrypt(passwd)
			filename_encrypt = filedirname[:-4]+'_encrypted'+'.pdf'
			#print(filename_encrypt)
			resultPdf = open(filename_encrypt,'wb')
			pdfWriter.write(resultPdf)
			resultPdf.close()
			

		

