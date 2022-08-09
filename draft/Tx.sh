#!/bin/bash

echo "26" > /sys/class/gpio/export
sleep 1
echo "out" > /sys/class/gpio/gpio26/direction
#output=$(./ultrasonic.py)
echo "1" > /sys/class/gpio/gpio26/value
echo "26" > /sys/class/gpio/unexport
