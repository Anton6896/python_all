import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="log_logging.txt"
)


# disable all log in one line of code ( CRITICAL one of 5 levels of logging )
logging.disable(logging.CRITICAL)


def fac(n):
    # bad func to calculat factorial 
    logging.debug("start fac  :")
    tot = 1
    for i in range(1, n + 1):
        tot *= i
        logging.debug(f"in loop tot : {tot}")
    return tot


if __name__ == "__main__":
    logging.debug("start code ")
    print(f"factor : {fac(5)}")

    logging.debug("end code")
