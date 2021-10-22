class Person:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

    def __str__(self):
        return f"[ name {self.name}, id: {self.id} ]"


class PersonFactory:
    _id = -1

    @staticmethod
    def create_person(name):
        PersonFactory._id += 1
        print(f'create person with id {PersonFactory._id}')
        return Person(PersonFactory._id, name=name)


if __name__ == "__main__":
    p1 = PersonFactory.create_person('person 1')
    p2 = PersonFactory.create_person('person 2')
    p3 = PersonFactory.create_person('person 3')

    print()
    print(p1)
    print(p2)
    print(p3)
