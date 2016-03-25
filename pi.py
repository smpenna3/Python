#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import time
import spidev
import os

USERNAME = "parkerraspberrypi@gmail.com"
PASSWORD = "Panthers1995"
MAILTO = "Smpenna3@gmail.com"

subject = "Too hot!"

msg = MIMEText('The server is becoming too warm!')
msg['Subject'] = subject
msg['From'] = USERNAME
msg['To'] = MAILTO


spi = spidev.SpiDev()
spi.open(0,0)
temp_sensor = 0
delay = 5
temp_limit = 25

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data


def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts


def ConvertTemp(data,places):
 
  # ADC Value
  # (approx)  Temp  Volts
  #    0      -50    0.00
  #   78      -25    0.25
  #  155        0    0.50
  #  233       25    0.75
  #  310       50    1.00
  #  465      100    1.50
  #  775      200    2.50
  # 1023      280    3.30
 
  temp = ((data * 330)/float(1023))-50
  temp = round(temp,places)
  return temp


def sendmail():
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo_or_helo_if_needed()
		server.starttls()
		server.ehlo_or_helo_if_needed()
		server.login(USERNAME,PASSWORD)
		server.sendmail(USERNAME, MAILTO, msg.as_string())
		print("Warning Sent")
		server.quit() 
	except:
		print("Send failed")


while True:
	temp_reading = readChannel(temp_sensor)
	temp_volts = ConvertVolts(temp_reading, 2)
	temperature = ConvertTemp(temp_volts, 2)
	print('--------------------------------')
	print(temperature)

	if(temperature >= temp_limit):
		print('Temperature too hot!')
		sendmail()
		break

	time.sleep(delay)