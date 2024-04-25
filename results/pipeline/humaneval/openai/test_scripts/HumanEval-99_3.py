def closest_integer(value):
    value = value.strip()
    
    numerical_value = float(value)
    
    floor_value = int(numerical_value)
    ceil_value = int(numerical_value) + 1

    diff_floor = abs(numerical_value - floor_value)
    diff_ceil = abs(ceil_value - numerical_value)
    
    # Decide which integer is closer or return the farthest from zero if equidistant
    if diff_floor == diff_ceil:
        if numerical_value < 0:
            return ceil_value
        else:
            return floor_value
    elif diff_floor < diff_ceil:
        return floor_value
    else:
        return ceil_value

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)