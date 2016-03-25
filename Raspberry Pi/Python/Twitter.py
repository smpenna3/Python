# import necessary libraries, some of these will need to be installed on the pi
import time
from tweepy.auth import OAuthHandler
import tweepy

# import functions from keysRPI.py
from keysPython import *

# set the keys for twitter access from keysRPI.py
token = keys["token"]
token_secret = keys["token_secret"]
key = keys["key"]
secret = keys["key_secret"] 

# log into the twitter account using OAuthHandler and select the timeline using tweepy
auth = OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth) 
timeline = client.home_timeline()


def Check():
	# a function which checks the twitter feed for colors
	
	def checkfunction():
		for item in timeline:
			# Check every item in the timeline for a color in it
		    text = "%s says '%s'" % (item.user.screen_name, item.text)
		    for i in colors:
			    if(i in item.text):
			    	# if it finds a color print the color to the screen
			    	print i
			    	return
		print text
	

	checkfunction()

# run the check function
# twitter does have a limit to the API requests, a maximum of 30 per 15 minutes
# if this is exceeded it will not allow you to log in
Check()
