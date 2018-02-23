#! python3
# pdfParanoia - encrypts all PDFs in a folder and adds '_encrypted.pdf' to the filename

import PyPDF2, os, sys

path = sys.argv[1]
pw = sys.argv[2]
os.chdir(path)

for folderName, subfolders, filenames in os.walk('C:\\Users\\Rodrigo\\pdfs'):
	os.chdir(folderName)
	for filename in filenames:
		if filename.endswith('.pdf'):
			pdfFile = open(filename, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			pdfWriter = PyPDF2.PdfFileWriter()
			for pageNum in range(pdfReader.numPages):	# Copies current pdf object to a new pdf object
				pdfWriter.addPage(pdfReader.getPage(pageNum))
			pdfWriter.encrypt(pw)
			title, ext = os.path.splitext(filename)
			resultPdf = open(title + '_encrypted.pdf', 'wb')
			pdfWriter.write(resultPdf)
			resultPdf.close()
			# Checks to see if the file was encrypted correctly
			pdfReader = PyPDF2.PdfFileReader(open(title + '_encrypted.pdf', 'rb'))
			if pdfReader.decrypt(pw) == 1:
				print(filename,'successfully encrypted.')
			else:
				print(filename,'not encrypted.') 
			#os.unlink(filename)
