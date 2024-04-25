def is_woodall(x):
    if x <= 0:
        return False
    
    n = 1
    while True:
        woodall = 2 ** (n - 1) * n
        if woodall == x:
            return True
        elif woodall > x:
            return False
        n += 1

# Test cases




def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)