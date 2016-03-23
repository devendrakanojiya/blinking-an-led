import RPi.GPIO as GPIO
import time
from random import randint
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
count = 0
while (count < 9):
	print 'The count is:', count
	count = count + 1
	print "LED on"
	GPIO.output(18,GPIO.HIGH)
	time.sleep(1)
	print "LED off"
	GPIO.output(18,GPIO.LOW)
	time.sleep(1)
