class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Persion:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.actions = Event()

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'

    def do_action(self):
        self.actions(self.name, self.age)  # call all the functions in the list

def action_2(name, age):
    print(f'{name} is {age} years old, have action 2')


if __name__ == '__main__':
    person = Persion('Sherlock', 20)
    person.actions.append(action_2) # add function to the list
    person.actions.append(lambda name, age: print(f'{name} is {age} years old, have action 1'))
    person.do_action()

    print('remove action 2')
    person.actions.remove(action_2) # remove function from the list
    person.do_action()