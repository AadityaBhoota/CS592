import math

def find_Index(n):
    k = 1
    while True:
        triangular_number = k * (k + 1) // 2
        if int(math.log10(triangular_number)) + 1 >= n:
            return k
        k += 1

def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)