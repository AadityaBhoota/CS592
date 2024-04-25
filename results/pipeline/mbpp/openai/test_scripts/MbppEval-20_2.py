import math

def is_woodall(x):
    if x <= 0:
        return False

    n = 1
    woodall_num = n * x - 1

    while woodall_num < x:
        n += 1
        woodall_num = n * x - 1

    if woodall_num == x:
        return True

    return False

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)