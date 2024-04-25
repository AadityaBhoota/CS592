def closest_integer(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string")

    try:
        num = float(value)
    except ValueError:
        raise ValueError("Input must be a valid number")

    return round(num)

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)