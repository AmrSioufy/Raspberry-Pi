#!/usr/bin/python3

#These are the define variables
#import time
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.cleanup()
#GPIO.setup(17, GPIO.IN)

from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo =17, trigger=4, threshold_distance=0.5)

#When properties to add more tasks when ultrasonic range progress
#def inrng():
#	print("In range")
#
#def outrng():
#	print("Out of range")
#
#ultrasonic.when_in_range = inrng
#ultrasonic.when_out_of_range = outrng
#input("Press ctrl+c to exit")

#Wait property for action sensing
while True:
	ultrasonic.wait_for_in_range()
	print("In range")
	ultrasonic.wait_for_out_of_range()
	print("Out of range")

#while True:
#	distance = 0
#	while GPIO.input(17) == 0:
#		pulse_start = time.time()
#	while GPIO.input(17) == 1:
#		pulse_end = time.time()
#	pulse_duration = pulse_end - pulse_start
#	distance = pulse_duration * 17150
#	distance = round(distance, 2)
#
#print ("Distance: ", distance, "cm")
