import math

def find_Index(n):
    digit = math.ceil(n * math.log10(10))
    res = 10 ** (digit - 1)
    
    while True:
        if math.isqrt(8 * res + 1) ** 2 == 8 * res + 1:
            triangular = (-1 + math.isqrt(8 * res + 1)) // 2
            if len(str(triangular)) >= n:
                return res
        res += 1

# Test cases




def check(candidate):
    assert find_Index(2) == 4
    assert find_Index(3) == 14
    assert find_Index(4) == 45

check(find_Index)