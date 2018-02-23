#! python3
# webComicDL.py - Regularly checks websites for new comics and downloads them.

import requests, os, bs4, shelve, datetime

sites = ['http://www.moonbeard.com', 'http://www.lefthandedtoons.com']
mbFile = shelve.open('urls_mb')
lhFile = shelve.open('urls_lh')

def saveImg(comicUrl, shelfFile):
	res = requests.get(comicUrl)
	res.raise_for_status()
	# Save the image to desktop
	os.chdir('C:\\Users\\Rodrigo\\Desktop')
	imageFile = open(os.path.basename(comicUrl), 'wb')
	for chunk in res.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

def downloader(shelfFile, site, selector, comic):
	res = requests.get(site)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)

	# Find the url of the comic image.
	comicElem = soup.select(selector)
	if comicElem == []:
		print('Could not find comic image.')
	else:
		saveImg(comic, shelfFile)
		os.chdir('C:\\Users\\Rodrigo\\PythonScripts')

def main(shelfFile, site, selector):
	res = requests.get(site)
	res.raise_for_status
	soup = bs4.BeautifulSoup(res.text)
	comicElem = soup.select(selector)
	comicUrl = comicElem[0].get('src')

	if comicUrl == shelfFile['imageUrl']:
		return
	else:
		downloader(shelfFile, site, selector, comicUrl)
		shelfFile['imageUrl'] = comicUrl

if datetime.datetime.now() > datetime.datetime(2017, 10, 24, 21, 0, 0):
	main(mbFile, sites[0], '#comic img')
	main(lhFile, sites[1], '.comicdata img')		
else:
	mbFile['imageUrl'] = ''
	lhFile['imageUrl'] = ''
	main(mbFile, sites[0], '#comic img')
	main(lhFile, sites[0], '.comicdata img')
	mbFile.close()
	lhFile.close()
