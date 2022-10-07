import random
import string


class User_1:
    def __init__(self, name) -> None:
        self.name = name


class User_2:
    strings = []

    def __init__(self, full_name: str) -> None:
        self.names = [self.get_or_add(s) for s in full_name.split(' ')]

    def get_or_add(self, s: str) -> int:
        if s in self.strings:
            return self.strings.index(s)

        self.strings.append(s)
        return len(self.strings) - 1

    def __str__(self) -> str:
        return ' '.join([self.strings[x] for x in self.names])

    @property
    def show_size(self) -> int:
        return len(self.strings)


def r_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(5)])


if __name__ == '__main__':
    users = []
    f_name = [r_string() for x in range(100)]
    l_name = [r_string() for x in range(100)]

    for fn in f_name:
        for ln in l_name:
            users.append(User_2(f'{fn} {ln}'))

    print(len(users))
    print(User_2('').show_size)
