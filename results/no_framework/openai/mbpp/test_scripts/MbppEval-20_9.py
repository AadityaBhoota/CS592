def is_woodall(x):
    for k in range(2, x):
        if x == k * (2**k) - 1:
            return True
    return False

# Test cases




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)