import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    largest_prime = 2  # Step 0
    # Step 1
    for i in range(2, math.isqrt(n) + 1):  # Step 2 corrected
        if n % i == 0:
            # Step 3
            if is_prime(i):
                # Step 4
                largest_prime = i  # Update largest_prime
    return largest_prime  # Step 5



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)