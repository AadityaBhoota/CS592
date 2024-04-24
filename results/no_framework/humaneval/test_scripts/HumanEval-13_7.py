def greatest_common_divisor(a: int, b: int) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

# Test the function





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