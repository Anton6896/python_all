import threading
import time

x = 8192

"""
### limiting access to resource 
using lock (acquire , release)
one thread at the time can access resource 
"""

lock = threading.Lock()

# threading


def my_double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        time.sleep(1)
        print(f"f1 : {x}")
    print("got to maximum")
    lock.release()


def my_halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        time.sleep(1)
        print(f"f2 : {x}")
    print("minimum get")
    lock.release()


id = 1


def my_semafore(thread_number):
    semafore = threading.BoundedSemaphore(value=5)
    global id

    print(f"{thread_number} -- getting access \t <-- {id}")
    id += 1
    semafore.acquire()
    print(f"{thread_number} -- access granted \t>!<")
    # do some work here
    time.sleep(10)
    print(f"{thread_number} -- release sequence \t--> {id}")
    semafore.release()
    id -= 1


event = threading.Event()


def event_my():
    print("waiting for event")
    event.wait()

    # working here
    print("event is happent , now working ... ")
    


if __name__ == "__main__":
    # t1 = threading.Thread(target=my_double)
    # t2 = threading.Thread(target=my_halve)
    # t1.start()
    # t2.start()

    # for thread_number in range(1,11):
    #     t = threading.Thread(target=my_semafore, args=(thread_number, ))
    #     t.start()
    #     time.sleep(1)


    # Events and Daemon Threads
    """ event will .wait() till .set() not activated  """
    t1 = threading.Thread(target=event_my)
    t1.start()

    if (input("\nenter y / n ") == 'y'):
        event.set()
