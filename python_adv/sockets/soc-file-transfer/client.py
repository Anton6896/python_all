import os 
import socket

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_soc.connect(('localhost', 9999))

with client_soc as sender:
    with open('pic1.png', 'rb') as file_to_transfer:
        data = file_to_transfer.read()
        file_size = os.path.getsize('pic1.png')

    sender.send('pic1.png'.encode())
    sender.send(str(file_size).encode())
    # sender.sendall(data)
    # sender.send('<endfileant>'.encode())
