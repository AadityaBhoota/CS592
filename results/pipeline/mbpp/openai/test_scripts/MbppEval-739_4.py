import math

def find_Index(n):
    index = 1
    
    while True:
        triangular_number = index * (index + 1) / 2
        
        if len(str(triangular_number)) < n:
            index += 1
        else:
            if len(str(triangular_number)) == n:
                return index
            else:
                index += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)