import time #required for pausing the script
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import requests
import os
import json
from gpiozero import DistanceSensor
import photo
import identify
import centralmotor
import motor3
import itemsensor
import door

#an object has been put in the bin, rotate, and identify the object
def binstatus1(items):
    print("Checking item")
    object = itemsensor.itemsensor()
    print("Checking door")
    open = door.door()
    while object == False and open == True:
        print("Checking item2")
        object = itemsensor.itemsensor()
        print("Checking door2")
        open = door.door()
    if object == True:
        print("rotating the plate")
        centralmotor.anticlock() #rotate objects in the top compartment 90 degrees and update items
        photo.photo() #capture image of the object and assign it to variable
        a = identify.identify() #identify object in the image captured
        time.sleep(7) #wait 7 seconds for object identification
        items[1] = a #assign object type to compartments array
        print(items)
        return(items)
    if object == False and open == False:
        return(items)

#the door is closed, empty any compartments which contain items
def binstatus2(items, holes):
    while items != [0,0,0,0]:
        #for each element of the items array
        for i in range(1, 4):
            #if object matches compartment category, empty the compartment
            if items[i-1] == 'Metal can':
                holestarget = [1,0,0,0]
            if items[i] == 'Plastic Bottle':
                holestarget = [0,1,0,0]
            if items[i+1] == 'tbd':
                holestarget = [0,0,1,0]
            if items[i+2] == 'tbd':
                holestarget = [0,0,0,1]
            turning = [a + b for a,b in zip(holes, holestarget)]
            if turning == [1,0,0,1]:
                motor3.clock()
            if turning == [0,1,0,1]:
                motor3.clock()
            if turning == [0,0,1,1]:
                motor3.clock()
            if turning == [0,0,0,2]:
                motor3.clock()

            items = [items[3], items[0], items[1], items[2]]
    return(items)

    motor3.run()

#initialise items array
items = [0,0,0,0]
holes = [0,0,0,1]
print(items)
print("Checking door")
open = door.door()
#if an object has been input to the bin, rotate and identify it
if open == True:
    print("going to binstatus1")
    items = binstatus1(items)
    binstatus2(items, holes)

#check if another object is about to be input to the bin
#open = door.door()
#while the door is open wait for object to be input or door to close
if open == False:
    binstatus2(items)
