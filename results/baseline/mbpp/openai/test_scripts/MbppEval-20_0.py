def is_woodall(x):
    if x < 2:
        return False

    n = 1
    woodall = 1
    while woodall < x:
        woodall = n * (2**n) - 1
        if woodall == x:
            return True
        n += 1

    return False

# Test the function with the given examples




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)