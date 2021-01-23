"""
binary index tree
"""
from copy import deepcopy
import gmpy


def lsb(x):
    """
    Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    print(bin(x))
    print((x & -x).bit_length() - 1)
    return (x & -x).bit_length() - 1


if __name__ == '__main__':
    lsb(10)
