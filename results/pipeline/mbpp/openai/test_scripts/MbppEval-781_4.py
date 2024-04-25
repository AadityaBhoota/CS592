import math

def count_divisors(n):
    sqrt_n = math.ceil(math.sqrt(n))
    count = 0

    count += 1  # counting 1 as a divisor

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            count += 2

    if sqrt_n * sqrt_n == n:
        count -= 1  # correcting as sqrt(n) should not be counted twice

    return "Even" if count % 2 == 0 else "Odd"

def check(candidate):
    assert count_divisors(10)
    assert not count_divisors(100)
    assert count_divisors(125)

check(count_divisors)