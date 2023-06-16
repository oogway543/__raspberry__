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
        sleep(0.2)
        blue.stop()
        green.stop()
        red.stop()
        sleep(0.1)

        blue.start(i)
        sleep(0.2)
        blue.stop()
        sleep(0.1)

        green.start(i)
        sleep(0.2)
        green.stop()
        sleep(0.1)

        red.start(i)
        sleep(0.2)
        red.stop()
        sleep(0.1)

        red.start(i)
        blue.start(i)
        sleep(0.2)
        red.stop()
        blue.stop()
        sleep(0.1)

        green.start(i)
        blue.start(i)
        sleep(0.2)
        green.stop()
        blue.stop()
        sleep(0.1)

        red.start(i)
        green.start(i)
        sleep(0.2)
        red.stop()
        green.stop()
        



except KeyboardInterrupt:
    blue.stop()
    red.stop()
    green.stop()   
    GPIO.cleanup()
    print("Program is stopped")
    
