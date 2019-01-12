import RPi.GPIO as GPIO
import time

#rotate the top bin compartment
def rotate():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6,GPIO.OUT)
    print ("LED on")
    GPIO.output(6,GPIO.HIGH)
    time.sleep(3)
    print ("LED off")
    GPIO.output(6,GPIO.LOW)
