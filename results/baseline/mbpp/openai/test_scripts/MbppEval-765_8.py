def is_polite(n):
    primes = []
    p = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(p)
        p += 1

    nth_polite = primes[n - 1] + n
    return nth_polite

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)