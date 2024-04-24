def closest_integer(value):
    number = float(value)
    ceil_num = int(number + 0.5)
    floor_num = int(number - 0.5)

    if number - floor_num < ceil_num - number:
        return floor_num
    elif number - floor_num > ceil_num - number:
        return ceil_num
    else:
        if number >= 0:
            return ceil_num
        else:
            return floor_num

# Test cases
print(closest_integer("10"))   # Output: 10
print(closest_integer("15.3")) # Output: 15
print(closest_integer("14.5")) # Output: 15
print(closest_integer("-14.5")) # Output: -15

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)