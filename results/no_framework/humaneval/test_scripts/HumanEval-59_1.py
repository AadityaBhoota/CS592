from math import isqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    for i in range(isqrt(n), 1, -1):
        if n % i == 0 and is_prime(i):
            return i

# Test the function with examples





METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)