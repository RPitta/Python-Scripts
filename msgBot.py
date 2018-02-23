#! python3
# msgBot.py - Sends a select group of people on your friends list a message.
#			  Specify the email address on the command line.			  

import pyautogui, time, sys

FRIENDS = []

for email in range(1, len(sys.argv)):
	FRIENDS.append(sys.argv[email])

NEW_CONVO_BUTTON = (134, 185)
NEW_CONVO_COLOR = (15, 157, 88)
MESSAGE = input('Enter a message to send:\n')

# Gives you 2 seconds to put the window in focus
while not pyautogui.pixelMatchesColor(NEW_CONVO_BUTTON[0], NEW_CONVO_BUTTON[1], NEW_CONVO_COLOR):
	i = 0
	for i in range(4):
		print('Window not in focus' + '.' * i, end='')
		print('\b' * 22, end='', flush=True)
		time.sleep(1)
	

print('OK')
pyautogui.PAUSE = 0.5

for name in FRIENDS:
	pyautogui.click(NEW_CONVO_BUTTON[0], NEW_CONVO_BUTTON[1])
	pyautogui.typewrite(name)
	pyautogui.press('enter')
	pyautogui.typewrite(MESSAGE)
	pyautogui.press('enter')
	print('Message sent to', name)


