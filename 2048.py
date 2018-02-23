#! python3
# 2048.py - Sends up, right, down, and left keystrokes to automatically play 2048

import bs4, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Use selenium to open 2048.
browser = webdriver.Chrome(executable_path=r'C:\\Users\\chromedriver.exe')
browser.get('https://gabrielecirulli.github.io/2048/')

gameElem = browser.find_element_by_tag_name('html')
gameOver = browser.find_element_by_class_name('retry-button')

# Send up, right, down, and left keys until game is over.
while not gameOver.is_displayed():
	gameElem.send_keys(Keys.UP)
	gameElem.send_keys(Keys.RIGHT)
	gameElem.send_keys(Keys.DOWN)
	gameElem.send_keys(Keys.LEFT)