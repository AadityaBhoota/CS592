def closest_integer(value):
    num = float(value)
    if num // 1 == num:  # If the number is already an integer
        return int(num)
    else:
        floor_int = int(num // 1)
        ceil_int = int(num // 1) + 1
        
        if abs(num - floor_int) < abs(num - ceil_int):
            return floor_int
        else:
            return ceil_int

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