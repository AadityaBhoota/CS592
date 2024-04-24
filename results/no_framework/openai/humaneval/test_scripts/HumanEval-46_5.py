def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    prev_values = [0, 0, 2, 0]
    
    for i in range(4, n+1):
        current = prev_values[0] + prev_values[1] + prev_values[2] + prev_values[3]
        prev_values = [prev_values[1], prev_values[2], prev_values[3], current]
    
    return prev_values[-1]

# Test cases






METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)