import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep


if __name__ == "__main__":
  print("Hello world")
  mcp3008 = zero.MCP3008(channel=7)
  try:
    while True:
       value = round(mcp3008.value*100)
       print("light", value)
       if value > 20:
         print("go")


       sleep(1)  
  except KeyboardInterrupt:
    GPIO.cleanup()
    print("bye~")
