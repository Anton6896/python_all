import random


class Db:
    _instance = None

    def __init__(self):
        id = random.randint(1, 100)
        print('id = ', id)

    # running before __init__
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Db, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    # can see that this is the same class cls but __init__ is running twice !!
    # this is bad sign for the singleton cls
    d1 = Db()
    d2 = Db()

    print(d1 == d2)
