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
#    ser.write('Serial Communication Using Raspberry Pi\r\n')
#    ser.write('By: Embedded Laboratory\r\n')
    print ("Data Echo Mode Enabled")
    while True:
        if ser.inWaiting() > 0:
            data = ser.read()
            print (data)

#except KeyboardInterrupt:
#    print ("Exiting Program")

#except:
#    print ("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass
