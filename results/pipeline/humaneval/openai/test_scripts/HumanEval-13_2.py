def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b """
    smallest = min(a, b)
    for i in range(smallest, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1  # Default return if no common divisor found



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12

check(greatest_common_divisor)