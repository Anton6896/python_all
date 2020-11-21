import threading


def one():
    print('\n')
    for _ in range(50):
        print("hello world", end=" ")
    print('\n')

def two():
    for _ in range(50):
        print("-------   ", end=" ")
    print('\n')

def three():
    for _ in range(50):
        print("other world", end=" ")
    print('\n')


if __name__ == "__main__":
    t1 = threading.Thread(target=one)
    t2 = threading.Thread(target=two)
    t3 = threading.Thread(target=three)


    t1.start()
    t1.join()  # whait toll t1 finish 
    t2.start()
    t3.start()

