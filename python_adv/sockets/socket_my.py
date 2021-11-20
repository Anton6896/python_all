import socket

# create socket for the tcp connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 55555))
s.listen()

while True:
    client, address = s.accept()
    print(f"connected to address : {address}")
    # must send the message with encode ()
    client.send("you are connected".encode())
    client.close()  # prevent to many clients
