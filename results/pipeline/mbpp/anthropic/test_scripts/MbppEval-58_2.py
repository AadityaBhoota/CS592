def opposite_Signs(x, y):
    if (x > 0 and y < 0) or (x < 0 and y > 0):
        return True
    else:
        return False

def check(candidate):
    assert opposite_Signs(1,-2) == True
    assert opposite_Signs(3,2) == False
    assert opposite_Signs(-10,-10) == False
    assert opposite_Signs(-2,2) == True

check(opposite_Signs)