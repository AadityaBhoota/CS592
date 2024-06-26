def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    
    a, b, c, d = 0, 0, 2, 0
    
    for i in range(2, n):
        d = a + b + c
        a, b, c = b, c, d
    
    return d

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)