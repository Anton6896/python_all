"""
seperate chaining for collision problems
"""
from ClassData import Some


class Table:
    def __init__(self, amount: int):
        # init new table with "amount" of buckets with 0 as empty indicator
        self.table = [0 for i in range(amount)]
        self.table_max_size = amount

    def push(self, obj):
        # todo crete dynamic allocation for buckets if bucket is to
        #  big reallocate the size of main hash table )
        if self.table[self._util_get_hash(obj)] == 0:
            self.table[self._util_get_hash(obj)] = []  # <- create new bucket
            self.table[self._util_get_hash(obj)].append(
                obj)  # <- store whole obj (pointer)
        else:
            # this bucket is not empty  ( collision handler )
            self.table[self._util_get_hash(obj)].append(obj)

        return self

    def _util_add_size_to_table(self):
        """
        # this is optional ( to implement )
        # crete new table , make new hash for all values
        # return new bigger table to user as self
        """
        pass

    def is_inside(self, obj: Some):
        # check if obj is in table
        if self.table[self._util_get_hash(obj)] == 0:
            return False

        # in bucket one or more than one obj
        elif len(self.table[self._util_get_hash(obj)]) == 1:
            # for an obj can be only one hash value !
            # for an value many objects (collision)
            return True

        else:
            # have an collision , look in bucket for obj
            for obj_i in self.table[self._util_get_hash(obj)]:
                if obj_i.get_val() == obj.get_val():
                    return True

        return False

    def pop(self, obj: Some):
        """
        remove by id of object 
        """
        if self.table[self._util_get_hash(obj)] == 0:
            # empty bucket
            return False

        elif len(self.table[self._util_get_hash(obj)]) == 1:
            # obj fount and obj alone in bucket , -> 0
            self.table[self._util_get_hash(obj)] = 0
            return True

        else:
            # loop thru the bucket objects
            for i in range(len(self.table[self._util_get_hash(obj)])):
                if self.table[self._util_get_hash(obj)][i].get_val() == obj.get_val():
                    # remove by index 
                    del(self.table[self._util_get_hash(obj)][i])





    def show_all(self):
        # loop thru the table and show all objects
        for i, obj_list in enumerate(self.table):
            print(f"----- bucket {i}:")
            if obj_list != 0:
                for obj in obj_list:
                    print(f"\t {str(obj)}")
            else:
                print("empty - ")


    def _util_get_hash(self, obj: Some):
        # using classData as obj that have value for hashing (as example)  <- get_val()
        # return value in range of max table size ( hash )  <- of course this is an super BAD function !!!
        # but this all for idea not for production use
        return (obj.get_val() * 24) % self.table_max_size

