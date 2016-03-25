The Raspberry Pi folder includes the email and twitter code for a raspberry pi

The email program will check an email address for "on" or "off" in the subject line
and change the state of an LED connected to a GPIO pin.

DO NOT use your personal gmail account with this program

To use you must enable access to less secure apps under gmail security, which can put
your account at risk.  Only used with a throw-away account with no important information


The twitter program will check a twitter timeline for colors, and set the color of an LED
based upon this.  There are eight colors which it checks for, defined in the keysRPI.py 
file.  To use this code a twitter developer account must be set up to receive a key and
token which can be entered into the keysRPI.py file to use, and can be gotten from https://apps.twitter.com.  There is a limit on the API requests you can do, 30 per 15 minutes or around every thirty seconds.  If this limit is
exceeded you are locked out from the API for 15 minutes.

The Python folder includes programs which can be run on any computer with python installed, and not just the raspberry pi.  The difference of course being the GPIO pins which normal computers don’t have, so the python compiler will not recognize those commands.  In the regular python versions the LED states/colors will just be printed to the screen instead of issuing a GPIO command.