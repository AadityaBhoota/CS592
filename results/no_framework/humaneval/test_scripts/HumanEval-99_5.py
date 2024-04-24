def closest_integer(value):
    # Convert the input value to a float
    num = float(value)
    
    # Get the floor and ceiling values of the number
    floor_value = int(num)
    ceil_value = int(num) + 1
    
    # Calculate the absolute differences between the number and the floor/ceiling values
    diff_floor = abs(num - floor_value)
    diff_ceil = abs(num - ceil_value)
    
    # Determine the closest integer based on the absolute differences
    if diff_floor < diff_ceil:
        return floor_value
    elif diff_floor > diff_ceil:
        return ceil_value
    else:
        # If equidistant, round away from zero
        if num >= 0:
            return ceil_value
        else:
            return floor_value

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