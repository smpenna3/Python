from Tkinter import *
import feedparser
import smtplib
from email.mime.text import MIMEText
#import RPi.GPIO as GPIO
import time
import imaplib

USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"

#root = Tk()



def getmail():
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	
	if(unread_count >= 1):
		for i in range(0, unread_count):

			if(response['items'][i].author_detail.name == "Google"):
				print("Notification Found")
				#Enable the notification for weather



	if(unread_count == 0):
		print("No Notifications Found")
		return None


	#change the dates so that it lines up with today.
	obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
	obj.login('parkerraspberrypi@gmail.com', 'Panthers1995')
	obj.select('Inbox')
	typ, data = obj.search(None, '(SINCE 11-Jun-2015)')
	for num in data[0].split():
   		obj.store(num, '+FLAGS', '\\Seen')
		

'''
define the functions to do stuff with the Notifications
'''

'''
if(time == something):
	getmail()

if(time.seconds == 0):
	update clock
'''