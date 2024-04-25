import math

def next_Perfect_Square(N):
    sqrt = math.sqrt(N)
    if sqrt.is_integer():
        return int(sqrt + 1) ** 2
    else:
        return int(math.ceil(sqrt)) ** 2

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)