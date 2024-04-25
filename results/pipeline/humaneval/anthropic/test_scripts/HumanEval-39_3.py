def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    fib = [0, 1]
    i = 2
    while True:
        next_fib = fib[i-1] + fib[i-2]
        fib.append(next_fib)
        if is_prime(next_fib):
            if n == 1:
                return next_fib
            n -= 1
        i += 1



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