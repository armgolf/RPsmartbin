import RPi.GPIO as GPIO
import time
from threading import Thread
GPIO.setmode(GPIO.BCM)

def anticlock():
  control_pins = [8,11,9,10]
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(25):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.01)
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

def clock():
  control_pins = [10,9,11,8]
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(13):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.01)
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

def motor1():
  #control_pins = [4,17,27,22]
  control_pins = [22,27,17,4]
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(2250):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.0009)
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

def motor2():
  #control_pins = [12,16,20,21]
  control_pins = [21,20,16,12]
  for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
  halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ]
  for i in range(2250):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.0009)
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)

def run():
    Thread(target = motor1).start()
    Thread(target = motor2).start()
    Thread(target = clock).start()

clock()
anticlock()
clock()
