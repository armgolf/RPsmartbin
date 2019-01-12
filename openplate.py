#add completion of rotation variable and return it
import RPi.GPIO as GPIO
import time


#open and close plate specified in the argument
def openplate():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    print ("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    print ("LED off")
    GPIO.output(18,GPIO.LOW)
    #add complete variable for the plate and return it
