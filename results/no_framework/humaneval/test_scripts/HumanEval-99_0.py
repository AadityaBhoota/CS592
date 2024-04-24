def closest_integer(value):
    num = float(value)
    lower_int = int(num - 0.5)
    upper_int = int(num + 0.5)

    if num - lower_int < upper_int - num:
        return lower_int
    else:
        return upper_int

# Test cases





def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)