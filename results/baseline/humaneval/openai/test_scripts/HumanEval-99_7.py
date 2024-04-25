def closest_integer(value):
    num = float(value)
    ceil_num = int(num) if num >= 0 else int(num) - 1
    floor_num = ceil_num + 1
    return floor_num if num - ceil_num < floor_num - num else ceil_num

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