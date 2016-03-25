#!/usr/bin/env python

# Import necessary libraries.  These will need to be installed on the Pi
import feedparser
import time
import RPi.GPIO as GPIO
import imaplib

# Fill in the username and password of the email account between the quotes
# The gmail account must have advanced security features disabled, allow less secure apps
USERNAME = ""
PASSWORD = ""

# Make a new object for the gmail login using the username and password
obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login(USERNAME, PASSWORD)

def markread():
	# This function will mark all emails in the inbox as read in order to parse through
	# only new emails each time
            
    # Select the inbox for the object    
    obj.select('Inbox')
    
    # Search and store all emails that are marked 'UnSeen' which is unread to gmail
    typ ,data = obj.search(None,'UnSeen')
    
    # Replace the unread flag with seen to mark the email as read
    obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')


# Set the pin for the LED and setup GPIO pins
LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
 

while True:
	# Parse the inbox to find unread emails
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	# If there are unread emails check each email to see if there is a command in the subject
	if(unread_count != 0):
		for i in range(0,unread_count):
			# Print number of unread emails
			print"(" + str((i+1)) + "/" + str(unread_count) + ")" + response['items'][i].title
			if(response['items'][i].title == 'On' or response['items'][i].title == 'on'):
				# If the subject is on, set the GPIO pin to high
				print('On')
				GPIO.output(LED, True)
				markread()
			elif(response['items'][i].title == 'Off' or response['items'][i].title == 'off'):
				# If the subject is off, set the GPIO pin to low
				print('Off')
				markread()
				GPIO.output(LED, False)
			else:
				print('No command found')
				markread()
	else:
                pass
                print('\n' + 'No unread mail found' + '\n')
        time.sleep(10)
