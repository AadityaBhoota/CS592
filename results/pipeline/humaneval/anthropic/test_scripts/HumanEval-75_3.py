def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Returns True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 100:
        primes = [p for p in range(2, 100) if is_prime(p)]
        for i in range(len(primes)):
            for j in range(i, len(primes)):
                for k in range(j, len(primes)):
                    if primes[i] * primes[j] * primes[k] == a:
                        return True
    return False

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