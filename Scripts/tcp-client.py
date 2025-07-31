#!/usr/bin/python3

# This script performs basic banner grabbing by connecting to a specified IP and port,
# then receiving and displaying the initial data sent by the service (assuming it's a big enough buffer - 1024 bytes).

import socket

# Asking for user input
target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port number: "))

# Socket creation
s = socket.socket()

# Attempting to connect
try:
    s.connect((target_ip, target_port))
    answer = s.recv(1024)
    print("Received data:", answer.decode(errors='ignore'))
except Exception as e:
    print("Error connecting or receiving data:", e)
finally:
    s.close()
