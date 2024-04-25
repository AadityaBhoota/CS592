import math

def find_Index(n): 
    num = 1
    while True:
        triangular = num * (num + 1) // 2
        digits = int(math.log10(triangular)) + 1

        if digits == n:
            return num

        num += 1

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)