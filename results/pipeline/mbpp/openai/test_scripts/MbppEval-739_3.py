import math

def find_Index(n):
    num = 0
    index = 0

    while True:
        num += 1
        index += 1
        triangular_number = (num * (num + 1)) // 2
        
        if int(math.log10(triangular_number) + 1) >= n:
            return index

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)