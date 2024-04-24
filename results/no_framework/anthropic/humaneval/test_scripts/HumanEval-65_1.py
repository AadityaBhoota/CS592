def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string
    x_str = str(x)
    
    # Get the length of the string
    length = len(x_str)
    
    # If the shift is greater than the length, return the digits reversed
    if shift > length:
        return x_str[::-1]
    
    # Perform the circular shift
    shifted_digits = x_str[-shift:] + x_str[:-shift]
    
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