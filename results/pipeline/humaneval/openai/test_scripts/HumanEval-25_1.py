from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    
    # Step 1: Check for factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Step 2: Check for odd primes
    p = 3
    while p*p <= n:
        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            p += 2

    # Step 3: Add the remaining prime factor if n is not 1
    if n > 1:
        factors.append(n)

    return factors



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(2) == [2]
    assert candidate(4) == [2, 2]
    assert candidate(8) == [2, 2, 2]
    assert candidate(3 * 19) == [3, 19]
    assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert candidate(3 * 2 * 3) == [2, 3, 3]

check(factorize)