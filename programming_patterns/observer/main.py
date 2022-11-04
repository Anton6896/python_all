from typing import Any


class MyEvent(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for i in self:
            i(*args, **kwds)


class Person1:
    def __init__(self, name) -> None:
        self.name = name
        self.events = MyEvent()
    
    def call_event(self):
        self.events('person_1_event')


class Person2:
    def __init__(self, name) -> None:
        self.name = name
        self.events = MyEvent()
    
    def call_event(self):
        self.events('person_2_event')

def call_handler(name: str):
    print(f'the name {name}')

if __name__ == '__main__':
    p1 = Person1('name1')
    p2 = Person2('name2')
    
    p1.events.append(call_handler)
    p2.events.append(call_handler)

    p1.call_event()
    p2.call_event()
    
    
