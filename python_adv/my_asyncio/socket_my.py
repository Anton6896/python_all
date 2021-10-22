import socket
from select import select


"""
Dabid Beazley 2015 PyCon

run thru the >>> nc localhost 5001
"""

tasks = []
to_read = to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5001))
    server_socket.listen()

    while True:
        yield ('read', server_socket)
        client_socket, address = server_socket.accept()
        print(f' -- conn from {address}')
        tasks.append(client(client_socket))


def client(client_socket: socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)

        if not request:
            break

        else:
            response = "client response -- "
            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            # select will return keys from dict (keys in this case is socket)
            # select can deside if socket is ready to use 
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, socket = next(task)

            if reason == "read":
                # push socket sd key and generator object as value 
                to_read[socket] = task

            if reason == "write":
                to_write[socket] = task

        except StopIteration:
            print('done .. ')


# run script 
tasks.append(server())
event_loop()
