import math

def find_Index(n):
    """
    Find the index of the smallest triangular number with n digits.

    Args:
        n (int): The number of digits.

    Returns:
        int: The index of the smallest triangular number with n digits.
    """
    # Calculate the smallest triangular number with n digits
    min_tri_num = 10 ** (n - 1)

    # Find the index of the smallest triangular number with n digits
    index = 1
    while True:
        tri_num = (index * (index + 1)) // 2
        if tri_num >= min_tri_num:
            return index
        index += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)