def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def prime_fib(n: int) -> int:
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num) and generate_fibonacci(num) == num:
            count += 1
    return num



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