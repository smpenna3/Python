from Tkinter import *
import feedparser
import smtplib
from email.mime.text import MIMEText

month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"

root = Tk()
root.title('Parker Raspberry Pi Email')

sender = Label(root, text='From', width=20, font=('Helvetica', 12, 'bold'))
sender.grid(row=1, column=0)

subject = Label(root, text='Subject', width=20, font=('Helvetica', 12, 'bold'))
subject.grid(row=1, column=1)

body = Label(root, text='Message', width=50, font=('Helvetica', 12, 'bold'))
body.grid(row=1, column=2)

timereceived = Label(root, text='Time', width=5, font=('Helvetica', 12, 'bold'), anchor=E)
timereceived.grid(row=1, column=3)

	

sendera = []
subjecta = []
bodya = []
timea = []

def getmail():
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	if(unread_count >= 1):
		for i in range(0, unread_count):
			sendera.append(Button(root, text=str(response['items'][i].author_detail.name), width=20, anchor=W, bd=0))
			sendera[i].grid(row=(i+2), column=0, sticky=W)

			subjecta.append(Button(root, text=str(response['items'][i].title), width=20, anchor=W, bd=0))
			subjecta[i].grid(row=(i+2), column=1, sticky=W)

			bodya.append(Button(root, text=str(response['items'][i].summary_detail.value), width=50, anchor=W, bd=0))
			bodya[i].grid(row=(i+2), column=2, sticky=W)

			timea.append(Label(root, text=(str(month[list(response['items'][i].updated_parsed)[1]]) + ' ' + str(list(response['items'][i].updated_parsed)[2])), anchor=E))
			timea[i].grid(row=(i+2), column=3, sticky=E)
	elif(unread_count == 0):
		nomail = Label(root, text='No New Mail')
		nomail.grid(row = 2, column = 0, columnspan=4)

getmail()


def sendmail():
	newmail = Toplevel()
	newmail.title('New Message')

	with open('emails.txt', 'r') as inf:
		emails = eval(inf.read())


	def sendcomplete():
		alert1 = Toplevel()

		complete = Label(alert1, text='Send Complete!')
		complete.grid(row=0, column=0)

		def returnto():
			root.focus_set()
			alert1.destroy()
			newmail.destroy()

		quit = Button(alert1, text='Quit', fg='red', command=returnto)
		quit.grid(row=1, column=0)


	def sendfail():
		alert2 = Toplevel()
		
		def returnmail():
			root.focus_set()
			alert2.destroy()

		def returnto():
			root.focus_set()
			alert2.destroy()
			newmail.destroy()

		failed = Label(alert2, text='Send Failed')
		failed.grid(row=0, column=0, columnspan=2)

		tryagain = Button(alert2, text='Try Again?', fg='green', command=returnmail)
		tryagain.grid(row=1, column=0)

		quit = Button(alert2, text='Quit', fg='red', command=returnto)
		quit.grid(row=1, column=1)


	def emailnotfound():
		print('the email could not be found')
		MAILTO = ''
		#tell them that the email wasn't found in the contacts list
		#ask if they want to add it to the list
		#incorporate the contacts program in this one
		#allow them to add new contacts and look at current ones
		#this should give them the option to add the email if they want if it wasn't found
		#if they don't want to add the email give them the option to return and type one in
		pass


	def sendemail():
	    
	    if('@' in str(to_box.get())):
	    	MAILTO = str(to_box.get())
	    elif(str(to_box.get()) in emails.keys()):
	    	MAILTO = emails[str(to_box.get())]
	    else:
	    	emailnotfound()

	    #throw an error for not finding email
	 
	    subject = str(subject_box.get())
	    message = str(body.get(1.0, END))

	    msg = MIMEText(message)
	    msg['Subject'] = subject
	    msg['From'] = USERNAME
	    msg['To'] = MAILTO
	     
	    try:
	        server = smtplib.SMTP('smtp.gmail.com:587')
	        server.ehlo_or_helo_if_needed()
	        server.starttls()
	        server.ehlo_or_helo_if_needed()
	        server.login(USERNAME,PASSWORD)
	        server.sendmail(USERNAME, MAILTO, msg.as_string())
	        server.quit()
	        sendcomplete() 
	    except:
	        sendfail()

	to = Label(newmail, text='To:')
	to.grid(row=0, column=0, sticky=W)

	subject = Label(newmail, text='Subject:')
	subject.grid(row=1, column=0, sticky=W)

	to_box = Entry(newmail, width=30)
	to_box.grid(row = 0, column = 1)

	subject_box = Entry(newmail, width=30)
	subject_box.grid(row=1, column=1)

	body = Text(newmail, height=15, width=40)
	body.grid(row=2, column=0, columnspan=2)

	send = Button(newmail, width=40, fg='green', command=sendemail, text='Send')
	send.grid(row=3, column=0, columnspan=2)


def showcontacts():
	contactwindow = Toplevel()
	contactwindow.title('Contacts')
	key = []
	value = []

	text = open('emails.txt', 'r')
	emails = eval(text.read())

	for i in range(0, len(emails.keys())):
		key.append(Label(contactwindow, text = str(emails.keys()[i]), width = 10, anchor = W))
		key[i].grid(row = (i+1), column = 0, sticky = W)

		value.append(Label(contactwindow, text = str(emails.values()[i]), width = 30, anchor = E))
		value[i].grid(row = (i+1), column = 1, sticky = W)

	text.close()


def addcontact():
	addcontactwindow = Toplevel()
	addcontactwindow.title('New Contact')

	def addtodictionary():
		text = open('emails.txt', 'r+')
		emails = eval(text.read())
		text.truncate()
		text.close()
		emails.update({nameentry.get(): emailentry.get()})
		text = open('emails.txt', 'w')
		text.write(str(emails))
		text.close()

		root.focus_set()
		addcontactwindow.destroy()


	name = Label(addcontactwindow, text='Name: ')
	name.grid(row = 0, column = 0)

	email = Label(addcontactwindow, text='Email: ')
	email.grid(row = 1, column = 0)

	nameentry = Entry(addcontactwindow, width=40)
	nameentry.grid(row = 0, column = 1)

	emailentry = Entry(addcontactwindow, width=40)
	emailentry.grid(row = 1, column = 1)

	submit = Button(addcontactwindow, text='Submit', width=40, command=addtodictionary)
	submit.grid(row=3, column=0, columnspan=3)


sendbutton = Button(root, text='Send new message', command=sendmail)
sendbutton.grid(row = 0, column = 0, sticky=W)

refresh = Button(root, text='Refresh', command=getmail)
refresh.grid(row = 0, column=3, sticky=E)

contactlist = Button(root, text='Contacts', command=showcontacts)
contactlist.grid(row = 0, column = 1)

newcontactbutton = Button(root, text='New Contact', command=addcontact)
newcontactbutton.grid(row = 0, column = 2)

root.mainloop()