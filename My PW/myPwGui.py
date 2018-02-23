#! python3
# myPwGui.py - An insecure password locker

from appJar import gui
import shelve, os, pyperclip

shelf = shelve.open('mainPw')
accFile = shelve.open('Accounts')

app = gui("myPw", "400x200")
app.setResizable(canResize=False)
app.setStretch("both")
app.setGuiPadding(15, 15)
app.setBg("lemon chiffon")
app.setFont(12, font=("Ubuntu Mono"))

def copyPw(btn):
	pyperclip.copy(accFile[btn])
	print(btn + ' pw copied to clipboard.')

def newScreen():
	app.removeEntry("Password")
	app.removeButton("Submit")
	app.addButton("Add", add, 1, 0)
	app.addButton("Delete", delete)
	app.addButton("Update", update)

def managePw():
	app.setLabel("title", "\tClick on an account name\nto copy its password to your clipboard.")
	if os.stat("Accounts.bak").st_size == 0:
		app.addLabel("L2", "Nothing here yet...")
		newScreen() 
	else:
		row = 1
		for account in accFile.keys():
			app.addButton(account, copyPw, row, 1)
			row += 1
		newScreen()	

def masterPw(btn):
	if 'pwd' not in shelf:
		pwd = app.getEntry("Password")
		shelf['pwd'] = pwd
		managePw()
	else:
		while True:
			pwd = app.getEntry("Password")
			# TODO: Retrybox
			if pwd == shelf['pwd']:
				break 	# Enter the locker
			else:
				app.addLabel("invalidPw", "Invalid password.")
				app.clearEntry("Password")
		managePw()		
		
def add(btn):
	account = app.textBox("Add", "Enter an account name:")
	if account != None:
		if account not in accFile:
			accFile[account] = pyperclip.paste()
			app.okBox("AddSuccess", "Account password added successfully.")
		else:
			app.okBox("AddDup", "That account has already been added.")

def update(btn):
	account = app.textBox("Update", "Enter the account name:")
	if account != None:
		if account not in accFile:
			# TODO: Retrybox
			app.okBox("UpFailed", "That account has not been added yet.\nRetry or click 'Add' to add accounts.")
		else:
			accFile[account] = pyperclip.paste()
			app.okBox("AddDup", account + " account has been updated successfully.")

def delete(btn):
	account = app.textBox("Delete", "Enter the account name.")
	if account != None:
		if account not in accFile:
			# make this a retry box
			app.okBox("DelFailed", "That account has not been added yet.\nRetry or click 'Add' to add accounts.")
		else:
			del accFile[account]
			app.okBox("DelSuccess", account + " account has been deleted successfully.")

app.addLabel("title", "My Password Locker", 0, 0, 2)
app.addLabelSecretEntry("Password")
app.addButton("Submit", masterPw)
app.enableEnter(masterPw)

app.go()
