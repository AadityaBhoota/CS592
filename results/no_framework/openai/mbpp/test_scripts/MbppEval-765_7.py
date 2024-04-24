import math

def is_polite(n):
    primes = [2]
    p = 3

    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if p % prime == 0:
                is_prime = False
                break
            if prime > math.isqrt(p):
                break
        if is_prime:
            primes.append(p)

        p += 1

    return primes[-1]

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)