def is_woodall(x):
    n = 0
    i = 0
    while 2**i - 1 < x:
        n += 2**i - 1
        i += 1
    return n == x

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)