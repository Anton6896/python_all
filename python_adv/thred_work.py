import threading


def one():
    for _ in range(50):
        print("hello world", end=" ")

def two():
    for _ in range(50):
        print("-------   ", end=" ")

def three():
    for _ in range(50):
        print("other world", end=" ")


if __name__ == "__main__":
    t1 = threading.Thread(target=one)
    t2 = threading.Thread(target=two)
    t3 = threading.Thread(target=three)

    # will take kare about race com=ndition and lock by it self c
    t1.start()
    t2.start()
    t3.start()

