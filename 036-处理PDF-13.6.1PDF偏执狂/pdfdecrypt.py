import PyPDF2,os

passwd = input('please input decrypted password:')
filedirname = ''
for folderName, subfolders, filenames in os.walk('.'):
	#读取文件下所有的pdf文件
	for filename in filenames:
		if filename.endswith('.pdf'):
			filedirname = folderName +'/'+ filename
			pdfReader = PyPDF2.PdfFileReader(open(filedirname, 'rb'))
			
			if pdfReader.isEncrypted == True:  #判断pdf是否被加密
				try:
					pdfReader.decrypt(passwd)    #解密pdf
					numPages = pdfReader.numPages   #读取pdf页数
					
				except PyPDF2.utils.PdfReadError:   #读取失败说明解密失败，报错
					print(filename + ", decrypted password is not correct.")
				else:     #解密成功，复制pdf内容，生成新文件
					pdfWriter = PyPDF2.PdfFileWriter()
					for pageNum in range(numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))
					filename_decrypt = filedirname[:-14]+'_decrypted'+'.pdf'
					resultPdf = open(filename_decrypt,'wb')
					pdfWriter.write(resultPdf)
					resultPdf.close()


		

