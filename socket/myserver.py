#!/usr/bin/python3

import os
import socket
import tqdm
import sys

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

myhost = '192.168.1.222'
host = '192.168.234.128'
port = 50000
filename = "test.txt"
filesize = os.path.getsize(filename)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"[+] Connecting as {myhost}:{port}")
s.connect((host, port))

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()
