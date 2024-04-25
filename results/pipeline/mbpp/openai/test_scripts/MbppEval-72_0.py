def dif_Square(n):
    if int(n**0.5) ** 2 == n:
        return True
    else:
        limit = int(n**0.5)
        for x in range(1, limit+1):
            y_square = x*x - n
            if y_square >= 0 and int(y_square**0.5) == y_square**0.5:
                return True
        return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)