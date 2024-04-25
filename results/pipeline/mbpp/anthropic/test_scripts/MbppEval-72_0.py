def dif_Square(n):
    a = 0
    b = 1
    while b**2 - a**2 < n:
        a += 1
        b += 1
    return b**2 - a**2 == n

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)