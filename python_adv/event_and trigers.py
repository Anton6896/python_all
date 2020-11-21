import threading
from threading import Event, Thread
event = Event()


def working():
    print("waiting for event, stop working")
    event.wait()
    print("continue working ")


if __name__ == "__main__":
    t1 = Thread(target=working)
    t1.start()

    if (input("enter y/n -->  ") == 'y'):
        print("got trigger")
        event.set()
