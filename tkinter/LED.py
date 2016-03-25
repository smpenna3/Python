from Tkinter import *
import smtplib
from email.mime.text import MIMEText
 
USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"
MAILTO = 'parkerraspberrypi@gmail.com'

root = Tk()

def Send(subject):
	message = ''
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = USERNAME
	msg['To'] = MAILTO

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo_or_helo_if_needed()
	server.starttls()
	server.ehlo_or_helo_if_needed()
	server.login(USERNAME,PASSWORD)
	server.sendmail(USERNAME, MAILTO, msg.as_string())
	print("Send complete")
	server.quit()

def On():
	Send('1')
	print('On')

def Off():
	Send('0')
	print('Off')

on = Button(root, text='On', command=On, fg='Green', width=10)
on.pack()

off = Button(root, text='Off', command=Off, fg='Red', width=10)
off.pack()

root.mainloop()