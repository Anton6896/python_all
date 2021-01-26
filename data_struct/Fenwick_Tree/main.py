"""
Binary Indexed Tree or Fenwick Tree
"""
from copy import deepcopy

"""
[3,4,-2,7,3,11,5,-8,-9,2,4,-8]      <- data for testing
[3,7,-2,12,3,14,5,23,-9,-7,4,-11]   <- fenwick tree
"""


class FT:

    def __init__(self, arr_new):
        self.arr_ft = deepcopy(arr_new)  # <- for manipulations
        self.ft_init()

    def ft_init(self):
        for i in range(len(self.arr_ft)):  # <- from 1 to max size
            # get lsb from 1 to len() + (my position 0 base )
            p_idx = self.lsb(i + 1) + i

            if p_idx < len(self.arr_ft):
                self.arr_ft[p_idx] = (self.arr_ft[i] + self.arr_ft[p_idx])

            print(f"i :{i} \t-> lsb:{self.lsb(i+1)} , parent : {p_idx} ")

        print(self.arr_ft)

    def lsb(self, x) -> int:
        """
        Returns the less significant bit at input number
        ! numbers in range 128 bit operator -> [1, 2, 4, 8, 16, 32, 64, 128]
        """

        idx = (x & -x).bit_length() - 1
        if idx < 0:
            return 1
        bp = [1, 2, 4, 8, 16, 32, 64, 128]

        # print(f"bin(x)  -> {bin(x)}")
        # print(f"bin(-x) -> {bin(-x)}")
        # print(f"bin(x & -x) -> {bin(x & -x)}")  # <- last set bit
        # print(f"lowest value in binary for {x} :-> {bp[idx]}")
        return bp[idx]


if __name__ == '__main__':
    ft = FT([3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8])
