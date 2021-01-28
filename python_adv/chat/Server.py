import socket
import threading
from collections import namedtuple

HOST = '127.0.0.1'
PORT = 9090


class Server:
    # util
    # =====================================================================
    def __init__(self):

        #  users - > ( client , nickname  )
        # client - serer object
        # nickname - user name
        self.users = []

        # INET - internet socket , SOCK_STREAM -tcp
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
        print("server started")

    def __del__(self):  # <- destructor
        print("\tserver is stopped ...")

    def push_client(self, client, nickname):
        self.users.append((client, nickname))

    def get_client_idx(self, client):
        for i, n in enumerate(self.users):
            if n[0] is client:
                return i

    def pop_client(self, obj):
        self.users.pop(self.get_client_idx(obj))

    # server
    # ------------------------------------------------------------------------

    def broadcast(self, message):
        for _ in self.users:
            _[0].send(message)  # <- to client obj

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f"connected with address {address}")

            client.send("NICK".encode("utf-8"))
            nickname = client.recv(1024)
            print(f"new nick : {nickname} connected")
            self.push_client(client, nickname)

            self.broadcast(f"{nickname} added to chat ".encode("utf-8"))
            client.send(f"Connected to server".encode("utf-8"))

            thread = threading.Thread(target=self.handler, args=(client,))
            thread.start()

    def handler(self, client):
        while True:
            try:
                message = client.recv(1024)
                print(f"{self.users[self.get_client_idx(client)][1]} --> {message}")
                self.broadcast(message)

            except ConnectionError:
                print(f"{self.users[self.get_client_idx(client)][1]} :: living a chat ")
                self.pop_client(client)
                client.close()
                break  # <- stop an function and exit from thread


if __name__ == '__main__':
    server = Server()
    server.receive()
