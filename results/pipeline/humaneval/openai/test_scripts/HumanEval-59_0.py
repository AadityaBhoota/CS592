#!/usr/bin/env python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    largest_prime = 2
    i = 2
    while i <= n:
        if n % i == 0:
            n //= i
            if is_prime(n):
                largest_prime = n
        else:
            i += 1
    return largest_prime






METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)