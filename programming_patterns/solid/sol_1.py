import os
import pathlib

"""
solid design principles (Robert C Martin)
1. srp -> singel responsibility for object 
2.
3.
4.
5.
"""


class Journal:
    # responsibility is keep journal and his entry's

    # responsibility is ok  --------------
    def __init__(self):
        self.entries = []
        self.counter = 0

    def add_entry(self, text):
        self.counter += 1
        self.entries.append(f"{self.counter} : {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # brake responsibility of class ------------
    # def save_self(self, name):
    #     os.chdir(os.getcwd)

    #     try:
    #         with open(name, "w") as f:
    #             f.write(str(self))
    #             print('done writing')
    #     except:
    #         print('cant write it')

    # def load (self):
    #     pass

    # def etc(self):
    #     pass


# right way to implement the single responsibility rule
class PersistanceManager:
    # handle Journal class needs
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        f_path = str(pathlib.Path(__file__).parent.absolute())+"/"+filename
        try:
            with open(f_path, "w") as f:
                f.write(str(journal))
                print('done writing')
        except:
            print('cant write it')


if __name__ == "__main__":
    j = Journal()

    j.add_entry('entry 1')
    j.add_entry('entry 2')
    j.add_entry('entry 3')
    print(j)

    print()
    j.remove_entry(1)
    print(j)
    PersistanceManager.save_to_file(j, 'my.txt')

    
