#!/

GPIO.setmode(GPIO.BCM)

import RPi.GPIO as GPIO
from time import sleep



GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
blue = GPIO.PWM(17, 70)
while True:
    i = 0
    if(i<70):
        i+=1
    else:
        i=0 
    blue.start(i)
    sleep(0.5)
    blue.stop()
    sleep(0.5)
    GPIO.cleanup()
