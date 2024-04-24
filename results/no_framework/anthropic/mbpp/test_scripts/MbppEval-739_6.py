import math

def find_Index(n):
    """
    Write a python function to find the index of the smallest triangular number with n digits.
    
    Parameters:
    n (int): The number of digits to find the smallest triangular number for.
    
    Returns:
    int: The index of the smallest triangular number with n digits.
    """
    # Calculate the first triangular number with n digits
    first_n_digits = 10 ** (n - 1)
    index = 1
    while True:
        triangular_num = (index * (index + 1)) // 2
        if triangular_num >= first_n_digits:
            return index
        index += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)