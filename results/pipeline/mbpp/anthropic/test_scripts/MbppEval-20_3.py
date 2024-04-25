import math

def is_woodall(x):
    result = 2 ** x + x
    sqrt = int(math.sqrt(result))
    return sqrt * sqrt == result

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)