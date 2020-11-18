import threading


def one():
    print("hello world")

def two():
    for i in range(10):
        print("other world", end=" ")


if __name__ == "__main__":
    t1 = threading.Thread(target=one)
    t2 = threading.Thread(target=two)
    
    t1.start()
    t2.start()
