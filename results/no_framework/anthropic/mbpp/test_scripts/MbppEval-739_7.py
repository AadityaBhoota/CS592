import math

def find_Index(n):
    """
    Write a python function to find the index of smallest triangular number with n digits.
    Examples:
    find_Index(2) == 4
    find_Index(3) == 14
    find_Index(4) == 45
    """
    # Start with the first triangular number (1)
    index = 1
    triangular_number = 1

    # Iterate until we find the smallest triangular number with n digits
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index

    return index

# Test the function




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)