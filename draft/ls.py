#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 23
GPIO.setup(LIGHT_PIN, GPIO.IN)
lOld = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)
while True:
  if GPIO.input(LIGHT_PIN) != lOld:
    if GPIO.input(LIGHT_PIN):
      print ('No Braking detected!')
    else:
      print ('Braking detected!')
  lOld = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
