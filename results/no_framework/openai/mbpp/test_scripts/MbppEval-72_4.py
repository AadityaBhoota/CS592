def dif_Square(n):
    for i in range(1, n//2 + 1):
        square = i*i
        if square < n and (n - square)**0.5 % 1 == 0:
            return True
    return False

# Test cases




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)