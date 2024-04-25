def find(n, m):
    result = n // m
    return result

def check(candidate):
    assert find(10,3) == 3
    assert find(4,2) == 2
    assert find(20,5) == 4

check(find)