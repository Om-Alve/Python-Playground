import socket
CHUNK = 65535
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# OS will bind this for us
hostname = '127.0.0.1'

while True:
    s.connect((hostname, port))
    message = input("Type MEssage: ")
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Amadeus: {text}")
