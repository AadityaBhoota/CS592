import math

def find_Index(n):
    '''
    Write a python function to find the index of the smallest triangular number with n digits. 

    Parameters:
    n (int): Number of digits in the triangular number.

    Returns:
    int: Index of the smallest triangular number with n digits.
    '''
    triangular_num = lambda x: x * (x + 1) // 2
    index = 1
    while len(str(triangular_num(index))) < n:
        index += 1

    return index

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)