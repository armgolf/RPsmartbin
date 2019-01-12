import time #required for pausing the script
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import requests
import os
import json
from gpiozero import DistanceSensor
import photo
print("hello")
import identify
print("hello")
import motor3
print("hello")
#import openplate
import itemsensor
print("hello")
import door
print("hello")

GPIO.setmode(GPIO.BCM)
open = door.door()
object = itemsensor.itemsensor()
motor3.motor()
open = door.door()
object = itemsensor.itemsensor()
