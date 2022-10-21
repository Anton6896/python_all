class Person:
    def __init__(self, name: str):
        self.name = name
        self.chat_log: list[str] = []
        self.room: 'ChatRoom' = None

    def receive(self, sender: str, message: str):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)

    def say(self, message: str):
        self.room.broadcast(self.name, message)

    def private_message(self, who: 'Person', message: str):
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self):
        self.people: list[Person] = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)


    def join(self, person: Person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)


    def message(self, source: str, destination: Person, message: str):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == '__main__':
    room = ChatRoom()

    john = Person('John')
    jane = Person('Jane')

    room.join(john)
    room.join(jane)

    john.say('hi room')
    jane.say('oh, hey john')

    simon = Person('Simon')
    room.join(simon)
    simon.say('hi everyone!')

    jane.private_message('Simon', 'glad you could join us!')