def circular_shift(x, shift):
    num_str = str(x)
    num_digits = len(num_str)
    if shift < num_digits:
        shifted_digits = num_str[-shift:] + num_str[:-shift]
    else:
        shifted_digits = num_str[::-1]
    return shifted_digits

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)