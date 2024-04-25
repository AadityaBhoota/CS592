from typing import List

def factorize(n: int) -> List[int]:
    prime_factors = []
    
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors



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