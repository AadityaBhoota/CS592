def dif_Square(n): 
    for i in range(1, int(n**0.5) + 1):
        x = i*i
        if x < n and (n - x)**0.5 % 1 == 0:
            return True
    return False

# Test cases




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)