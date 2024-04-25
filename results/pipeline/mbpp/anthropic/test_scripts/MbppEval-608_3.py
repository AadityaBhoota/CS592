from math import comb

def bell_Number(n):
    if n == 0:
        return 1
    
    return sum(bell_Number(k) * comb(n, k) for k in range(n))

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)