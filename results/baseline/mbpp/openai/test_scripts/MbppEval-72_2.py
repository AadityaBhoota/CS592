def dif_Square(n): 
    # A number n can be represented as the difference of two squares if n + k is a perfect square
    for k in range(1, n):
        if (n + k) ** 0.5 == int((n + k) ** 0.5):
            return True
    return False

# Test the function with the provided examples




def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)