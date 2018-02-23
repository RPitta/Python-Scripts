#! python3
# linkVerification.py - A program that downloads every linked page on a page

import requests, bs4

# Download a page using requests.get()
myPage = requests.get('https://automatetheboringstuff.com/chapter11/')
myPage.raise_for_status()
myPageSoup = bs4.BeautifulSoup(myPage.text)
# Use bs4 to find every linked page
linkElems = myPageSoup.select('.calibre5 a')

for i in range(len(list((linkElems)))):
	try:
		url = linkElems[i].get('href')
		if 'http:' or 'https:' in url:
			myLink = requests.get(url)
		else:
			myLink = requests.get('http:' + url)
	except Exception as exc:
		print('There was a problem downloading this link: ' + str(exc))
