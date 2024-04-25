def closest_integer(value):
    value = float(value)
    floor_value = int(value)
    ceil_value = int(value) + 1
    diff_floor = abs(value - floor_value)
    diff_ceil = abs(value - ceil_value)
    
    if diff_floor == diff_ceil:
        return ceil_value if value > 0 else floor_value
    
    return ceil_value if diff_ceil < diff_floor else floor_value

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)