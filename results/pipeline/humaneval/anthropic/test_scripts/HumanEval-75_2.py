def is_multiply_prime(a):
    """Return True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 100:
        prime_factors = find_prime_factors(a)
        return len(prime_factors) == 3

def find_prime_factors(n):
    """Find all the prime factors of a given number."""
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 2:
        prime_factors.append(n)
    return prime_factors

def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


check(is_multiply_prime)