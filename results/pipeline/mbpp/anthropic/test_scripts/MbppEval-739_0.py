import math

def find_Index(n):
    index = 0
    triangular_number = 1

    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index + 1

    return index

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)