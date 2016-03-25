#!/usr/bin/env python
import feedparser
 
USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"
 
response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
unread_count = int(response["feed"]["fullcount"])
print('\n' + 'Unread Emails: ' + str(unread_count))


if (unread_count != 0):
	for i in range(0,unread_count):
		print(response['items'][i])
else:
	print('No unread mail found' + '\n')



'''
stuff = ['year', 'month', 'day', 'hour', 'min', 'sec']

if (unread_count != 0):
	for i in range(0,unread_count):
		stuffa = list(response['items'][i].updated_parsed)
		print(response['items'][i].updated_parsed)
else:
	print('No unread mail found' + '\n')

jesus = zip(stuff, stuffa)
print
print jesus
'''