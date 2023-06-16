#!/usr/bin/python3


import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)


GPIO.setup(27, GPIO.OUT)# set GPIO as output for green led
GPIO.setup(17, GPIO.OUT)# set GPIO as output for blue led
GPIO.setup(22, GPIO.OUT)# set GPIO as output for red led
blue = GPIO.PWM(17, 75)
green = GPIO.PWM(27, 75)
red = GPIO.PWM(22, 75)
i = 75
try:
    while (True):

        blue.start(i)
        green.start(i)
        red.start(i)
        blue.stop()
        green.stop()
        red.stop()

        blue.start(i)
        blue.stop()

        green.start(i)
        green.stop()

        red.start(i)
        red.stop()

        red.start(i)
        blue.start(i)
        red.stop()
        blue.stop()

        green.start(i)
        blue.start(i)
        green.stop()
        blue.stop()

        red.start(i)
        green.start(i)
        red.stop()
        green.stop()
        
        


except KeyboardInterrupt:
    blue.stop()
    red.stop()
    green.stop()   
    GPIO.cleanup()
    print("Program is stopped")
    
