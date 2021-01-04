
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def __str__(self): pass


class CodeBuilder:
    __root = Person()

    def __init__(self, root_name):
        self.root_name = root_name

    @property
    def add_field(self, type_, name_):
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == "__main__":
    cb = CodeBuilder('person').add_field('name', 'new_name')\
        .add_field('age', '33')

    print(cb)
