from gpiozero import DistanceSensor
from time import sleep

#proximity sensor to identify when the door is open or closed
def door():
    sensor = DistanceSensor(echo=24, trigger=23)
    open = False
    count = 0
    #check 5 times in 5 seconds, set object variable accordingly
    for x in range(5):
        dist = sensor.distance * 100
        print(dist)
        if dist > 5:
            count = count + 1
            if count == 2:
                open = True
                print("the door is ...")
                print(open)
        sleep(1)
        

    return(open)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

#door()
