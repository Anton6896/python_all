"""
Binary Indexed Tree or Fenwick Tree
"""
from copy import deepcopy
import gmpy


def lsb(x):
    """
    Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    print(f"bin(x)  -> {bin(x)}")
    print(f"bin(-x) -> {bin(-x)}")
    print(f"bin(x & -x) -> {bin(x & -x)}")  # <- last set bit
    print(f"bit length of (x & -x) -1  -> {(x & -x).bit_length() - 1}")
    return (x & -x).bit_length() - 1


if __name__ == '__main__':
    lsb(10)  # <- index of lowest element
