from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed the number of times corresponding to how many times it appears in the factorization.
    The input number should be equal to the product of all factors.
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    
    # Start with the smallest prime factor, 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for other prime factors, starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    
    # If n is still greater than 2, it must be a prime number
    if n > 2:
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