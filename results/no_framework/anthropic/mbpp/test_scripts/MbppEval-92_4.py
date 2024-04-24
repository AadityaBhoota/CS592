def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    Examples:
    is_undulating("1212121") == True
    is_undulating("1991") == False
    is_undulating("121") == True
    """
    n = str(n)  # Convert the input to a string
    if len(n) < 3:
        return False  # Numbers less than 3 digits are not considered undulating

    # Check if the digits alternate between increasing and decreasing
    is_increasing = True
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            return False  # Digits can't be the same
        if n[i] > n[i-1] and not is_increasing:
            return False  # Digits should alternate between increasing and decreasing
        is_increasing = not is_increasing

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)