import os
import socket
import tqdm

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

client, addr = server.accept()
file_name = client.recv(512).decode()
# print(f'{file_name}')
file_size = client.recv(512).decode()
print(f'{file_size}')
