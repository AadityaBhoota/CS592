def fib4(n: int):
    if n < 2:
        return 0
    
    fib_values = [0, 0, 2, 0]
    
    for i in range(4, n + 1):
        next_val = fib_values[0] + fib_values[1] + fib_values[2] + fib_values[3]
        fib_values = [fib_values[1], fib_values[2], fib_values[3], next_val]
    
    return fib_values[3]

# Test the function with the given examples
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)