#!/usr/bin/python3

import time
import serial

print ("Starting program")

ser = serial.Serial('/dev/serial0', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
time.sleep(1)
try:
#bytes("Hello World",'UTF-8')
    ser.write(bytes("Hello World",'UTF-8'))
finally:
    ser.close()
