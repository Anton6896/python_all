#! python3
import os
import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    # filename="log_logging.txt"
)


# for windows use
# creating the batch file

def pr():
    print(os.getcwd())

    logging.debug("start loop")
    if (len(sys.argv) > 1):
        for i in sys.argv:
            print(i)


if __name__ == "__main__":
    logging.debug("start")
    pr()
    logging.debug("stop")
