import socket
import socket

port = 3000
CHUNK = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Creates a socket object
# socket,socket(family,type)
# AF_INET is family of ipv4 ip addresses
# SOCK_DGRAM = UDP
print(s)

hostname = '127.0.0.1'  # ip address for local machine

s.bind((hostname, port))


print(f"Server is live on {s.getsockname()}")

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')
    print(f"Om: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    s.sendto(data, clientAdd)
