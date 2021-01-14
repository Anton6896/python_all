"""
implementing the singleton by using decorator
"""


def singleton_dec(class_):
    # decorator that got an class and store it in _instances
    # if class is already bin created that return it else create new class
    _instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)
        return _instances[class_]

    return get_instance


# dont forget enable decorator lol !!
@singleton_dec
class DataClass:
    def __init__(self):
        print("using data base ")


if __name__ == '__main__':
    d1 = DataClass()
    d2 = DataClass()  # <- init call only once ! for this class

    print(d1 is d2)
