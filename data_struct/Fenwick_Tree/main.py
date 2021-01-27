"""
Binary Indexed Tree or Fenwick Tree

very confusing because you have an binary rep based 1
and you have an regular for loops that based 0
must find an connection for proper slicing in the array

solution add [0] to start of tree array , then working with 1 base for all
"""
from copy import deepcopy
import unittest


class FT:

    def __init__(self, arr_new):
        # the 0 value if for appropriate counter in list (place holder)
        # bin counter will start from 1
        self.arr_data = [0] + deepcopy(arr_new)
        self.ft_init()

    def ft_init(self):
        for i in range(1, len(self.arr_data)):
            p_idx = self.lsb(i) + i

            if p_idx < len(self.arr_data):  # <- out of bound check
                self.arr_data[p_idx] = (self.arr_data[i] + self.arr_data[p_idx])

        print(self.arr_data)

    def getter(self):
        return self.arr_data

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

    def sum_range(self, from_idx, to_idx):
        """
        find prefix sum from from_idx, to_idx
        det an difference ()
        """

        return self._sum_prefix(to_idx) - self._sum_prefix(from_idx - 1)

    def _sum_prefix(self, idx):
        # return sum from index (0 --> idx)
        sum_ = 0
        while idx > 0:
            sum_ += self.arr_data[idx]
            idx = (idx - self.lsb(idx))

        return sum_

    def update_point(self, pos, value):
        # for update i need to update from current to up to top parent
        pass

    def remove_point(self, value):
        pass


class TestSum(unittest.TestCase):
    data = [3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8]  # < test data
    test_case = [0, 3, 7, -2, 12, 3, 14, 5, 23, -9, -7, 4, -11]  # < test case

    ft_1 = FT(data)
    check_this = ft_1.getter()

    def test_creation(self):
        self.assertEqual(TestSum.test_case, TestSum.check_this, "Should be ok")

    data2 = [1, 8, 5, 4, 15, 2, 11, 7]
    ft_2 = FT(data2)  # [1,9,5,18,15,17,11,53]
    sum_to_test = ft_2.sum_range(3, 8)

    def test_range_sum(self):
        self.assertEqual(TestSum.sum_to_test, 44, "Should  be 44")


if __name__ == '__main__':
    unittest.main()
