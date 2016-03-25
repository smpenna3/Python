#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
 
USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"
MAILTO = str(raw_input("To whom is this being sent? "))
 
subject = str(raw_input('Subject'))
message = str(raw_input('Message? '))

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
	print("Send complete")
	server.quit() 
except:
	print("Send failed")
