def closest_integer(value):
    num = float(value)
    lower_int = int(num)
    upper_int = lower_int + 1

    if num - lower_int < upper_int - num:
        return lower_int
    elif num - lower_int > upper_int - num:
        return upper_int
    else:
        if num >= 0:
            return upper_int
        else:
            return lower_int

# Test cases
print(closest_integer("10"))      # Output: 10
print(closest_integer("15.3"))    # Output: 15
print(closest_integer("14.5"))    # Output: 15
print(closest_integer("-14.5"))   # Output: -15

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)