def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string and then to a list of digits
    digits = list(str(x))
    
    # Determine the length of the list of digits
    n = len(digits)
    
    # Perform the circular shift
    if shift <= n:
        digits = digits[-shift:] + digits[:-shift]
    else:
        digits = digits[::-1]
    
    # Convert the list of digits back to a string and return it
    return ''.join(digits)

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)