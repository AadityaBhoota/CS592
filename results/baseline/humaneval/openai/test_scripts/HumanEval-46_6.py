def fib4(n: int):
    if n < 2:
        return 0
    
    fib_numbers = [0, 0, 2, 0]
    
    for i in range(4, n+1):
        fib_numbers[i % 4] = sum(fib_numbers) % 10

    return fib_numbers[n % 4]

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)