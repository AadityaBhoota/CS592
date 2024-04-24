import math

def is_triangular_number(num):
    n = int(math.sqrt(2*num))
    return n*(n+1)//2 == num

def find_Index(n):
    digits = 1
    index = 0
    found = False
    
    while not found:
        index += 1
        num = (index * (index + 1)) // 2
        digits = int(math.log10(num)) + 1
        
        if digits == n and is_triangular_number(num):
            found = True
    
    return index

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)