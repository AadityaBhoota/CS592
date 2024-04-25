import math

def find_Index(n):
    '''
    Write a python function to find the index of smallest triangular number with n digits. 
    Examples:
    find_Index(2) == 4
    find_Index(3) == 14
    find_Index(4) == 45
    '''
    index = 1
    num = 1
    triangular_number = 0

    while True:
        triangular_number += num
        num += 1
        if len(str(triangular_number)) >= n:
            return index
        index += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)