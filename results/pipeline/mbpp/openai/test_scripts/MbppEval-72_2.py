import math

def dif_Square(n): 
    for a in range(1, int(math.sqrt(n)) + 1):
        b = math.isqrt(a * a - n)
        if a * a - b * b == n:
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)