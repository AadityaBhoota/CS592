import math

def find_Index(n):
    i = 0
    triangular_number = 0
    
    while len(str(triangular_number)) < n:
        i += 1
        triangular_number += i
    
    return i

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)