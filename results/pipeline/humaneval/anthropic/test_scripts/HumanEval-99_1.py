def closest_integer(value):
    float_value = float(value)
    rounded = round(float_value)
    
    if abs(float_value - rounded) < 0.5:
        if float_value > 0:
            return rounded + 1
        else:
            return rounded - 1
    else:
        return rounded

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)