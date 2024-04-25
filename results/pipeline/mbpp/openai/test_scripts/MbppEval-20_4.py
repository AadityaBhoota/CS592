def is_woodall(x):
    k = 1
    while k * (2 ** k) - 1 < x:
        k += 1
    return k * (2 ** k) - 1 == x

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)