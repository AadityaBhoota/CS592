def truncate_number(number: float) -> float:
    """ Return the decimal part of the number. """
    return number - int(number)

# Test the function with the provided example
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