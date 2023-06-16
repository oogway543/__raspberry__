import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class RGBLed():
    def __init__(self,redpin,greenpin,bluepin):
        GPIO.setup(red_pin,GPIO.OUT)
        GPIO.setup(green_pin,GPIO.OUT)
        GPIO.setup(blue_pin,GPIO.OUT)
        self.red = (redpin,75)
        self.green = (greenpin,75)
        self.blue = (bluepin,75)

    def close(self):
        self.red.setup()
        self.green.setup()
        self.blue.setup()
        GPIO.cleanup()