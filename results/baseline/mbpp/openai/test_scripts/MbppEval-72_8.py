def dif_Square(n):
    for i in range(1, n):
        for j in range(1, i):
            if i**2 - j**2 == n:
                return True
    return False

# Test cases




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)