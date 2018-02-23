#! python3
# customSeatingCards.py - Generates a seating card for each guest.

import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('guestCards', exist_ok=True)
flowerIm = Image.open('flower.jpg')

with open('guests.txt') as guestList:
	for name in guestList.readlines():
		im = Image.new('RGBA', (288, 360), 'white')
		draw = ImageDraw.Draw(im)
		draw.line([(2, 2), (286, 2), (286, 358), (2, 358), (2, 2)], fill='black')
		timesFont = ImageFont.truetype('C:\\Windows\\Fonts\\times.ttf', 24) 
		draw.text((85, 90), name.strip(), fill='black', font=timesFont)
		im.paste(flowerIm, (90, 150))
		im.save('C:\\Users\\Rodrigo\\PythonScripts\\guestCards\\' + name.strip() + 'Card.png')
