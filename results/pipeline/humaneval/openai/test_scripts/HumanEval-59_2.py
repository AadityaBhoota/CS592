def largest_prime_factor(n: int):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

# Test cases
result1 = largest_prime_factor(13195)
result2 = largest_prime_factor(2048)

result1, result2



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)