def is_woodall(x):
    if x <= 0:
        return False

    n = 0
    while True:
        woodall = n * (2 ** n - 1)
        if woodall == x:
            return True
        elif woodall > x:
            return False
        n += 1

    return False

# Test the function




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)