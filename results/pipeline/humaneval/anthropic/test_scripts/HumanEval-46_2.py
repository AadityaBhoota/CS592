def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n < 4:
        return [0, 0, 2, 0][n]
    
    fib4_list = [0, 0, 2, 0]
    for i in range(4, n+1):
        next_fib4 = sum(fib4_list[-4:])
        fib4_list.append(next_fib4)
    
    return fib4_list[n]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)