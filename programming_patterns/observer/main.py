from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for i in self:
            i(*args, **kwds)


class Person1:
    def __init__(self, name) -> None:
        self.name = name
        self.events = Event()

    def call_event(self):
        self.events('person_1_event')


class Person2:
    def __init__(self, name) -> None:
        self.name = name
        self.events = Event()

    def call_event(self):
        self.events('person_2_event')


def call_handler(name: str):
    print(f'the name {name}')


"""
person auth to drive testing
"""


class PropertyObserver:
    def __init__(self):
        self.property_change = Event()


class Driver(PropertyObserver):
    def __init__(self, age: int = 0):
        super().__init__()  # init observer
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if self._age == new_age:
            return

        self._age = new_age
        self.property_change('age', {'age': new_age})  # create an event


class TrafficAuthority:
    def __init__(self, driver: 'Driver'):
        self.driver = driver
        driver.property_change.append(self.controller)  # subscription to events

    def controller(self, event_type, data):
        if event_type == 'age':
            if data.get('age') < 16:
                print('cant drive car till 16 or more')
            else:
                print('driver is ok')
                self.driver.property_change.remove(self.controller)
        else:
            return


if __name__ == '__main__':
    # p1 = Person1('name1')
    # p2 = Person2('name2')
    #
    # p1.events.append(call_handler)
    # p2.events.append(call_handler)
    #
    # p1.call_event()
    # p2.call_event()

    d = Driver()
    tc = TrafficAuthority(d)
    for age in range(13, 18):
        print(f'setting age {age}')
        d.age = age
