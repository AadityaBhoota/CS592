import math

def dif_Square(n):
    for i in range(1, int(math.sqrt(n))+1):
        difference = i**2 - n
        if math.sqrt(difference).is_integer():
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)