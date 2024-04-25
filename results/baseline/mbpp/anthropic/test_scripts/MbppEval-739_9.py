import math

def find_Index(n):
    """
    Write a python function to find the index of smallest triangular number with n digits.
    
    Examples:
    find_Index(2) == 4
    find_Index(3) == 14
    find_Index(4) == 45
    """
    i = 1
    while True:
        triangular_number = (i * (i + 1)) // 2
        if len(str(triangular_number)) >= n:
            return i
        i += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)