def dif_Square(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            if j**2 - i**2 == n:
                return True
    return False

# Test cases




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)