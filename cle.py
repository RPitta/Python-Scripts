#! python3
# cle.py - (command line emailer) takes an email address and string of text on the command line and
# 		   then logs into your email and sends an email of the string to the provided address.

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# log into email 
browser = webdriver.Chrome(executable_path=r'C:\\Users\\chromedriver.exe')
browser.get('https://mail.google.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('rodrigo.pittar@gmail.com')
emailElem.send_keys(Keys.ENTER)
pwElem = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.NAME, 'password')))
pwElem.send_keys('rodrigop96')
pwElem.send_keys(Keys.ENTER)

# Clicks compose
composeElem = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.ID, ':ha')))
composeElem.click()

# Types in the recipient's email address and the message
recipientElem = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.NAME, 'to')))
recipientElem.send_keys(sys.argv[1])
bodyElem = WebDriverWait(browser, 10).until(
	EC.presence_of_element_located((By.ID, ':n5')))
bodyElem.send_keys(' '.join(sys.argv[2:]))

# Sends
sendElem = browser.find_element_by_id(':lu')
sendElem.click()
browser.quit()
