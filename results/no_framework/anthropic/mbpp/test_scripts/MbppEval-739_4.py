import math

def find_Index(n):
    """
    Write a python function to find the index of smallest triangular number with n digits.
    Examples:
    find_Index(2) == 4
    find_Index(3) == 14
    find_Index(4) == 45
    """
    # Calculate the smallest triangular number with n digits
    min_digits = int(math.ceil(math.sqrt(10 ** (n - 1)))) * (int(math.ceil(math.sqrt(10 ** (n - 1)))) + 1) // 2
    
    # Find the index of the smallest triangular number with n digits
    index = 0
    while True:
        index += 1
        triangular = index * (index + 1) // 2
        if triangular >= min_digits:
            return index

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)