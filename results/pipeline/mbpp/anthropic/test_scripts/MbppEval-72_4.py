import math

def dif_Square(n):
    for x in range(int(math.sqrt(n)) + 1):
        if n == x**2 - (x-1)**2:
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)