def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    >>> largest_divisor(15)
    5
    """
    max_divisor = 1
    for i in range(n//2, 1, -1):
        if n % i == 0:
            max_divisor = i
            break
    return max_divisor



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

check(largest_divisor)