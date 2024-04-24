def fib4(n: int):
    if n < 2:
        return 0
    
    fib_values = [0] * max(4, n+1)
    fib_values[2] = 2
    
    for i in range(3, n+1):
        fib_values[i] = fib_values[i-1] + fib_values[i-2] + fib_values[i-3] + fib_values[i-4]
    
    return fib_values[n]

# Test the function






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)