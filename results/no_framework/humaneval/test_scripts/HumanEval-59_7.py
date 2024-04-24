def largest_prime_factor(n: int):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)