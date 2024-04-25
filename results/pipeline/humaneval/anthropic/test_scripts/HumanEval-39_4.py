def is_prime(n: int) -> bool:
    """
    Checks if a given number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n: int) -> bool:
    """
    Checks if a given number is a Fibonacci number.
    """
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    """
    fib_nums = [0, 1]
    i = 2
    while len(fib_nums) < n:
        fib_num = fib_nums[i-1] + fib_nums[i-2]
        if is_prime(fib_num):
            fib_nums.append(fib_num)
        i += 1
    return fib_nums[n-1]

def fibonacci(n: int) -> int:
    """
    Calculates the n-th Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



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