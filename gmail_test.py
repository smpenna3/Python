#!/usr/bin/env python
import feedparser
import time
import RPi.GPIO as GPIO
import imaplib

obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login('parkerraspberrypi@gmail.com', 'Panthers1995')


def markread():
	obj.select('Inbox')
	typ ,data = obj.search(None,'UnSeen')
	obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')


LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
 
USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"

while True:
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	if(unread_count != 0):
		for i in range(0,unread_count):
			#print"(" + str((i+1)) + "/" + str(unread_count) + ")" + response['items'][i].title
			if(response['items'][i].title == '1'):
				print('On')
				GPIO.output(LED, True)
				markread()
			elif(response['items'][i].title == '0'):
				print('Off')
				markread()
				GPIO.output(LED, False)
			else:
				print('No command found')
				markread()
	else:
		print('\n' + 'No unread mail found' + '\n')

	time.sleep(10)
