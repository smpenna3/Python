from Tkinter import *

root = Tk()
root.title('New Contact')

def newcontact():

	def addcontact():
		text = open('emails.txt', 'r+')
		emails = eval(text.read())
		text.truncate()
		text.close()
		emails.update({nameentry.get(): emailentry.get()})
		text = open('emails.txt', 'w')
		text.write(str(emails))
		text.close()

		root.destroy()


	name = Label(root, text='Name: ')
	name.grid(row = 0, column = 0)

	email = Label(root, text='Email: ')
	email.grid(row = 1, column = 0)

	nameentry = Entry(root, width=40)
	nameentry.grid(row = 0, column = 1)

	emailentry = Entry(root, width=40)
	emailentry.grid(row = 1, column = 1)

	submit = Button(root, text='Submit', width=40, command=addcontact)
	submit.grid(row=3, column=0, columnspan=3)

newcontact()
root.mainloop()