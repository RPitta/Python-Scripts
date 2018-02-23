#! python3
# txt2xlsx.py - reads in text files and inserts them into a spreadsheet

import openpyxl

textFile1 = open('C:\\Users\\Rodrigo\\text1.txt')
textFile2 = open('C:\\Users\\Rodrigo\\text2.txt')
textFile3 = open('C:\\Users\\Rodrigo\\text3.txt')

txtFiles = [textFile1.readlines(),textFile2.readlines(),textFile3.readlines()]
wb = openpyxl.Workbook()
sheet = wb.active

#Loops through the cells in the spreadsheet
for col in range(1, len(txtFiles) + 1):
	for row in range(len(txtFiles[col - 1])):
		sheet.cell(row=row+1, column=col).value = txtFiles[col - 1][row]

wb.save('txt2xlsx.xlsx')



