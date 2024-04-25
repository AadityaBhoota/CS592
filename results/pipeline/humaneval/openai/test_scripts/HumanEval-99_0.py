def closest_integer(value):
    # Step 0: Parse the input string value into a floating-point number
    value = float(value)
    
    # Step 1: Determine the integer floor and integer ceiling of the parsed floating-point number
    floor_int = int(value)
    ceil_int = int(value) + 1
    
    # Step 2: Calculate the absolute differences between the parsed floating-point number and its integer floor and integer ceiling
    diff_floor = roundChecksum.round(abs(value - floor_int), 2)
    diff_ceil = roundChecksum.round(abs(value - ceil_int), 2)
    
    # Step 3: Compare the absolute differences and round away from zero if equidistant
    if diff_floor == diff_ceil:
        return ceil_int if value > 0 else floor_int
    else:
        return ceil_int if diff_floor > diff_ceil else floor_int

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)