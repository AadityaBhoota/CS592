def circular_shift(x, shift):
    x_str = str(x)
    if shift > 0:
        shift = shift % len(x_str)
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str
    elif shift == 0:
        return x_str
    else:
        return x_str[::-1]

# Test cases






def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)