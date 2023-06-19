#!/usr/bin/python3
import rgbled
from time import sleep
import RPi.GPIO as GPIO

if __name__ == '__main__':
    rgb = rgbled.RGBLed(22,27,17)
    rgb.greenLight(second=5)
    rgb.redLight(second=5)
    rgb.blueLight(second=5)
    rgb.clean()