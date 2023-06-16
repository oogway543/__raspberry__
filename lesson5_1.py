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
while (True):
    red.start(i)
    sleep(0.5)
    red.stop()
    sleep(0.5)

    blue.start(i)
    sleep(0.5)
    blue.stop()
    sleep(0.5)

    green.start(i)
    sleep(0.5)
    green.stop()
    sleep(0.5)
GPIO.cleanup()
