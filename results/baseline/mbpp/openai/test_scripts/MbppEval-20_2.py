def is_woodall(x):
    if x <= 1:
        return False

    p = 1
    while True:
        woodall = p * (2**p) - 1
        if woodall == x:
            return True
        elif woodall > x:
            return False
        p += 1

# Test the function with examples




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)