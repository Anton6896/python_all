from os import error
import traceback
import os
import logging


def square_this(symbol="*", height=4, width=10):
    # throw an error if symbol more then 1
    if len(symbol) > 1:
        with open(str(os.getcwd()) + "/LOG_FILE.txt", "a") as f:
            try:
                raise error(" symbol must be the 1 length !!! ")
            except error as e :
                print(e)
                print(e, file=f)

    print(symbol * width)
    for _ in range(height-2):
        print(symbol + (" " * (width-2)) + symbol)
    print(symbol * width)

def assert_check(number ):
    # check if num > 10 else throw assert error 
    #! assert number > 10
    #!   AssertionError
    assert number > 10
    print("ok")

if __name__ == "__main__":
    # square_this(symbol="XX")
    assert_check(5)


