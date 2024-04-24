def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):  # Start from n-1 and go down to 1
        if n % i == 0:  # Check if i divides n evenly
            return i

# Test the function with the example given in the docstring




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