class Db:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # cls._instance = super(Db, cls).
            pass


if __name__ == '__main__':
    print('testing ')
