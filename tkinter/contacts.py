from Tkinter import *

root = Tk()
root.title('Contacts')

def contacts():
	key = []
	value = []

	text = open('emails.txt', 'r')
	emails = eval(text.read())

	for i in range(0, len(emails.keys())):
		key.append(Label(root, text = str(emails.keys()[i]), width = 10, anchor = W))
		key[i].grid(row = (i+1), column = 0, sticky = W)

		value.append(Label(root, text = str(emails.values()[i]), width = 30, anchor = E))
		value[i].grid(row = (i+1), column = 1, sticky = W)

	text.close()

contacts()
root.mainloop()