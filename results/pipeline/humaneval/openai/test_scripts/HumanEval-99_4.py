import math

def closest_integer(value):
    float_value = float(value)
    floor_value = math.floor(float_value)
    ceiling_value = math.ceil(float_value)
    
    distance_floor = abs(float_value - floor_value)
    distance_ceiling = abs(ceiling_value - float_value)
    
    if distance_floor <= distance_ceiling:
        return floor_value
    else:
        return ceiling_value

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)