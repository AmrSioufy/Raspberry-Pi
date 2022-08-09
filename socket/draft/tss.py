#!/usr/bin/python3

import socket
import os

process_out = "./DistanceSensor.py >> stream.txt"
conversion = "sed -e :a -e '$q;N;2,$D;ba' stream.txt > stream2.txt"
printing = "cat stream2.txt"
os.system(process_out)
os.system(conversion)
os.system(printing)


#with open('stream2.txt') as f:
#    contents = f.read()
#    print(contents)
