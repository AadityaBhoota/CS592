def find_lucas(n): 
    if n == 0:
        return 2
    elif n == 1:
        return 1

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)