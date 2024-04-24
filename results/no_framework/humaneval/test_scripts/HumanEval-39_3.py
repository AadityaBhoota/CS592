def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        
        if is_prime(next_fib):
            if len(fib_sequence) == n:
                return next_fib

# Testing the function








METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437


check(prime_fib)