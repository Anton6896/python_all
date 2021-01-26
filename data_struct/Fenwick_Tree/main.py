"""
Binary Indexed Tree or Fenwick Tree

very confusing because you have an binary rep based 1
and you have an regular for loops that based 0
must find an connection for proper slicing in the array
"""
from copy import deepcopy
import unittest


class FT:

    def __init__(self, arr_new):
        # the none value if for appropriate counter in list (place holder)
        # bin counter will start from 1
        self.arr_data = [None] + deepcopy(arr_new)

    def ft_create(self):
        for i in range(1, len(self.arr_data)):
            p_idx = self.lsb(i) + i

            if p_idx < len(self.arr_data):  # <- out of bound check
                self.arr_data[p_idx] = (self.arr_data[i] + self.arr_data[p_idx])

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

    def sum_range(self, f_idx, to_idx):
        # range queries
        pass


class TestSum(unittest.TestCase):
    """
    [3,4,-2,7,3,11,5,-8,-9,2,4,-8]      <- data for testing
    [3,7,-2,12,3,14,5,23,-9,-7,4,-11]   <- fenwick tree
    """
    data = [3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8]  # < test data
    test_case = [None, 3, 7, -2, 12, 3, 14, 5, 23, -9, -7, 4, -11]  # < test case

    ft = FT(data)
    check_this = ft.ft_create()

    def test_equality(self):
        self.assertEqual(TestSum.test_case, TestSum.check_this, "Should be ok")

    def test_sum(self):
        pass


if __name__ == '__main__':
    unittest.main()
