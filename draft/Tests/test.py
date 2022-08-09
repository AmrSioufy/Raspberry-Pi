#!/usr/bin/python3
import time
from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo =17, trigger=4, threshold_distance=0.5)

#When properties to add more tasks when ultrasonic range progress
#def inrng():
#       print("In range")
#
#def outrng():
#       print("Out of range")


#ultrasonic.when_in_range = inrng
#ultrasonic.when_out_of_range = outrng
#input("Press ctrl+c to exit")

#Wait property for action sensing
while True:
	ultrasonic.wait_for_in_range()
	pulseend = time.time()

	ultrasonic.wait_for_out_of_range()
	pulsestart = time.time()

	pulsetotal = pulseend - pulsestart
	distance = pulsetotal * 17150
	print ("Distance: ", distance, "cm")


