import threading
import time

x = 8192

"""
### limiting access to resource 
using lock (acquire , release)
one thread at the time can access resource 
"""

lock = threading.Lock()


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


semafore = threading.BoundedSemaphore(value=5)


def my_semafore(thread_number):
    print(f"{thread_number} -- getting access ...")
    semafore.acquire()
    print(f"{thread_number} -- access granted ...")
    # do some work here 
    time.sleep(10)
    print(f"{thread_number} -- release sequence ...")
    semafore.release()


if __name__ == "__main__":
    # t1 = threading.Thread(target=my_double)
    # t2 = threading.Thread(target=my_halve)
    # t1.start()
    # t2.start()

    for thread_number in range(1,11):
        t = threading.Thread(target=my_semafore, args=(thread_number, ))
        t.start()
        time.sleep(1)
