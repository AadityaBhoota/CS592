def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Generates the n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def prime_fib(n: int) -> int:
    """
    prime_fib returns the n-th number that is a Fibonacci number and is also prime.
    """
    i = 0
    count = 0
    while count < n:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
        i += 1
    return fibonacci(i - 1)



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