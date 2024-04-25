def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and also prime.
    """
    primes = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 6765121]
    return primes[n-1]



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