from Tkinter import *
import smtplib
from email.mime.text import MIMEText

root = Tk()

with open('emails.txt', 'r') as inf:
	emails = eval(inf.read())

def sendcomplete():
    root.quit
    alert1 = Toplevel()

    complete = Label(alert1, text='Send Complete!')
    complete.grid(row=0, column=0)

    quit = Button(alert1, text='Quit', fg='red', command=alert1.quit)
    quit.grid(row=1, column=0)


def sendfail():
	alert2 = Toplevel()
	
	def returnmail():
		root.focus_set()
		alert2.destroy()

	failed = Label(alert2, text='Send Failed')
	failed.grid(row=0, column=0, columnspan=2)

	tryagain = Button(alert2, text='Try Again?', fg='green', command=returnmail)
	tryagain.grid(row=1, column=0)

	quit = Button(alert2, text='Quit', fg='red', command=root.quit)
	quit.grid(row=1, column=1)


def sendemail():
    USERNAME = "parkerraspberrypi@gmail.com"
    PASSWORD = "Panthers1995"
    
    if('@' in str(to_box.get())):
    	MAILTO = str(to_box.get())
    elif(str(to_box.get()) in emails.keys()):
    	MAILTO = emails[str(to_box.get())]

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

to = Label(root, text='To:')
to.grid(row=0, column=0, sticky=W)

subject = Label(root, text='Subject:')
subject.grid(row=1, column=0, sticky=W)

to_box = Entry(root, width=30)
to_box.grid(row = 0, column = 1)

subject_box = Entry(root, width=30)
subject_box.grid(row=1, column=1)

body = Text(root, height=15, width=40)
body.grid(row=2, column=0, columnspan=2)

send = Button(root, width=40, fg='green', command=sendemail, text='Send')
send.grid(row=3, column=0, columnspan=2)

root.mainloop()