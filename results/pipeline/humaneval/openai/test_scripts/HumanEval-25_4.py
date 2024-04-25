from typing import List


def factorize(n: int) -> List[int]:
    factors = []  # Step 0
    
    p = 2  # Step 1

    while p <= n**0.5:  # Step 2
        if n % p == 0:  # Step 3
            factors.append(p)  # Step 3
            n //= p  # Step 3
        else:
            p += 1  # Step 3
            
    if n > 1:  # Step 4
        factors.append(n)  # Step 4

    return factors  # Step 4



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