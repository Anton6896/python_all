"""
hashtable with seperate chaining approch 
"""


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)  # <- gey key hash

    def equals(self, other: Entry):
        if self.hash != other.hash:
            return False

        return (self.hash == other.key)

    def __str__(self):
        return "entry : " + str(self.value)
