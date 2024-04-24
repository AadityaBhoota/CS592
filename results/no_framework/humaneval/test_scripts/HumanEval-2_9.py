def truncate_number(number: float) -> float:
    """Return the decimal part of a positive floating point number."""
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part

# Test the function with the given example
result = truncate_number(3.5)
print(result)  # Output: 0.5



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)