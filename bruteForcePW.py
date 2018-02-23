#! python3
# bruteForcePW.py - Tries every word in the english language to decrypt a pdf.

import PyPDF2, sys, os

path = sys.argv[1]
os.chdir('C:\\Users\\Rodrigo\\PythonScripts')
wordList = [line.rstrip() for line in open('dictionary.txt')]
print('Breaking in...')

pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
for word in wordList:
	if pdfReader.decrypt(word) == 1 or pdfReader.decrypt(word.lower()) == 1:
		print('Password:', word)
		break
	else:
		continue

print(wordList)



