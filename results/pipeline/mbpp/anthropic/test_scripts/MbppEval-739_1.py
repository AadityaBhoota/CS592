import math

def find_Index(n):
    index = 1
    triangular_num = 1
    while len(str(triangular_num)) < n:
        index += 1
        triangular_num = (index * (index + 1)) // 2
    return index

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)