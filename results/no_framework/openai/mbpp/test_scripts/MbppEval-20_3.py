def is_woodall(x):
    if x <= 0:
        return False

    for n in range(1, x):
        if n * 2**n - 1 == x:
            return True

    return False

# Test cases




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)