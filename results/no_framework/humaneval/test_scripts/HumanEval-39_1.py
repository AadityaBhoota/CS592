def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    def fibonacci():
        a, b = 0, 1
        yield a
        yield b
        while True:
            a, b = b, a + b
            yield b
    
    fib_gen = fibonacci()
    fib_num = next(fib_gen)
    prime_fib_count = 0
    
    while prime_fib_count < n:
        if is_prime(fib_num):
            prime_fib_count += 1
        fib_num = next(fib_gen)
    
    return fib_num

# Test cases








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