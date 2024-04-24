import math

def find_Index(n):
    count = 0
    index = 1
    while True:
        triangular_number = index*(index+1)//2
        digits = int(math.log10(triangular_number)) + 1
        if digits == n:
            count += 1
            if count == 1:
                return index
        index += 1





def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)