def largest_divisor(n: int) -> int:
    divisor = 1
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisor = i
    
    return divisor



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