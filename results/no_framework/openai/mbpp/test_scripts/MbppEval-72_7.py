def dif_Square(n): 
    for i in range(1, n):
        if i*i < n:
            j = int((n + i*i)**0.5)
            if j*j == n + i*i:
                return True
    return False

# Test cases




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)