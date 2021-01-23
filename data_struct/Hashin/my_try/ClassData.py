"""
Hashable class that holds numbers (some data for example)
"""


def counter():  # <- static value
    return counter.value


class Some:
    counter.value = 0

    def __init__(self, data_):
        self.data = data_
        counter.value += 1
        self.c = counter()

    def get_val(self):
        return self.c

    def __str__(self):
        return f"my id {self.c}, my data is :{self.data}"
