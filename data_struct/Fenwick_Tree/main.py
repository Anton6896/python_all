"""
Binary Indexed Tree or Fenwick Tree
"""
from copy import deepcopy


def lsb(x):
    """
    Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    idx = (x & -x).bit_length() - 1
    arr = [1, 2, 4, 8, 16, 32]
    print(f"bin(x)  -> {bin(x)}")
    print(f"bin(-x) -> {bin(-x)}")
    print(f"bin(x & -x) -> {bin(x & -x)}")  # <- last set bit
    print(f"lowest value in binary : {arr[idx]}")
    print(f"bit length of (x & -x) -1  -> {idx}")
    return (x & -x).bit_length() - 1


if __name__ == '__main__':
    lsb(10)  # <- index of lowest element
