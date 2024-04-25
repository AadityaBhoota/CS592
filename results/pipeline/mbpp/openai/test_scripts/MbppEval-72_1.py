def dif_Square(n): 
    for a in range(int(n**0.5)+1):  # Square root limit to avoid duplicates
        b_square = a**2 - n
        if b_square >= 0:
            b = int(b_square**0.5)
            if b**2 == b_square and a > b and isinstance(a, int) and isinstance(b, int):
                return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)