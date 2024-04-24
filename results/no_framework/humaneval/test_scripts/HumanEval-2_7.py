def truncate_number(number: float) -> float:
    """Return the decimal part of the given number."""
    return number % 1

# Test the function
print(truncate_number(3.5))  # Output should be 0.5



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)