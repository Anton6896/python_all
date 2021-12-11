import random
import string


class User:
    acc = []

    def __init__(self, name: str):
        self.names = [self.get_or_add(x) for x in name.split(' ')]  # name indexes

    def get_or_add(self, name):
        if name in self.acc:
            return self.acc.index(name)
        else:
            self.acc.append(name)
            return len(self.acc) - 1

    @classmethod
    def get_total_acc(cls):
        return len(cls.acc)

    def __str__(self):
        return ' '.join([self.acc[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))

    print(len(users))
    print(User.get_total_acc())
