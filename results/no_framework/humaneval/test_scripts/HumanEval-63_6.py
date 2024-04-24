def fibfib(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        result = 0
    elif n == 2:
        result = 1
    else:
        result = fibfib(n-1, memo) + fibfib(n-2, memo) + fibfib(n-3, memo)
    
    memo[n] = result
    return result

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927


check(fibfib)