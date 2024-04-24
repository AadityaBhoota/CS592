def truncate_number(number: float) -> float:
    # Convert the floating point number to a string and split it at the decimal point
    integer_part, decimal_part = str(number).split('.')

    # Convert the decimal part back to a float
    return float('0.' + decimal_part)

# Test the function with the example provided in the docstring
print(truncate_number(3.5))  # Output: 0.5



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)