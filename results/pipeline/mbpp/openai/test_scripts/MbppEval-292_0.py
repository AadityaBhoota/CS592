def find(n, m):
    quotient = n // m
    return quotient

def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4

check(find)