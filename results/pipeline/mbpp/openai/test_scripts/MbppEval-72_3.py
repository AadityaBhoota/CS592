def dif_Square(n): 
    if n < 0:
        return False
    
    a = 1
    b = 1
    
    while a**2 - b**2 <= n:
        if a**2 - b**2 == n:
            return True
        elif a**2 - b**2 < n:
            a += 1
        else:
            b += 1
            a = b + 1
    
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)