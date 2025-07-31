#!/usr/bin/python3

import socket

# This script is inspired by an example from the book "Linux Basics for Hackers" by OccupyTheWeb
# It has been adapted to be more generic and interactive, for educational purposes only.

def main():
    # Ask the user for the IP address to bind to (e.g. 0.0.0.0 for all interfaces)
    TCP_IP = input("Enter the IP address to bind the server (e.g. 0.0.0.0): ").strip()

    # Ask the user for the port to listen on
    while True:
        try:
            TCP_PORT = int(input("Enter the port number to listen on (e.g. 6996): ").strip())
            if 1 <= TCP_PORT <= 65535:
                break
            else:
                print("Please enter a valid port number between 1 and 65535.")
        except ValueError:
            print("Please enter a numeric port number.")

    # Ask the user for buffer size
    while True:
        try:
            BUFFER_SIZE = int(input("Enter buffer size in bytes (e.g. 1024): ").strip())
            if BUFFER_SIZE > 0:
                break
            else:
                print("Please enter a positive integer for buffer size.")
        except ValueError:
            print("Please enter a numeric value for buffer size.")

    # Create the socket with IPv4 and TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print(f"Listening on {TCP_IP}:{TCP_PORT}...")

    conn, addr = s.accept()
    print(f"Connection established from: {addr}")

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print("Connection closed by client.")
            break
        print(f"Received data: {data}")
        # Echo the received data back to client
        conn.send(data)

    conn.close()
    s.close()
    print("Server closed.")

if __name__ == "__main__":
    main()
