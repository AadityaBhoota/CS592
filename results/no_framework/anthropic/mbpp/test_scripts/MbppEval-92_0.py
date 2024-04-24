def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    Args:
        n (str): The input number as a string.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    # Convert the input to a string if it's not already
    n = str(n)

    # Check if the length of the number is less than 3, as undulating numbers must have at least 3 digits
    if len(n) < 3:
        return False

    # Initialize a flag to keep track of the current trend (increasing or decreasing)
    is_increasing = None

    # Iterate through the digits of the number
    for i in range(1, len(n)):
        # If the current digit is equal to the previous digit, the number is not undulating
        if n[i] == n[i-1]:
            return False

        # Determine the current trend
        if n[i] > n[i-1]:
            if is_increasing is False:
                return False
            is_increasing = True
        else:
            if is_increasing is True:
                return False
            is_increasing = False

    # If the loop completed without returning False, the number is undulating
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)