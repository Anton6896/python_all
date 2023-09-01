class SingleMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class DB(metaclass=SingleMeta):
    def __init__(self):
        print('i am singe class')


if __name__ == '__main__':
    db1 = DB()
    db2 = DB()

    print(db1 == db2)
    print(db1 is db2)
