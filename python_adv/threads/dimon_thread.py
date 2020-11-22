from os import truncate
import threading
import time
import pathlib

# demon threading  == thread that run in back
# ground not depends for programme run time
my_file = str(pathlib.Path(__file__).parent.absolute()) + \
    "/files/text_file.txt"

my_text = ""


def read_file():
    global my_file, my_text
    while True:
        with open(my_file, "r") as f:
            my_text = f.read()
        time.sleep(3)


def print_loop():
    global my_text

    for i, _ in enumerate(range(30)):
        print(f"{i}__" + my_text)
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=read_file, daemon=True)
    t2 = threading.Thread(target=print_loop)

    t1.start()
    t2.start()
