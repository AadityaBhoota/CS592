import math

def dif_Square(n):
    if n % 4 != 1:
        return False

    x = int(math.ceil(math.sqrt(n)))
    y = int(math.floor(math.sqrt(n)))
    while x**2 - y**2 != n:
        if x**2 - y**2 < n:
            x += 1
        else:
            y -= 1

    return True

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)