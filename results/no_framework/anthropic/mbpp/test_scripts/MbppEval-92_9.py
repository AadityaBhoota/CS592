def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    Args:
        n (str): The number to be checked.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    if len(n) < 2:
        return False

    # Convert the input to a string if it's not already
    n = str(n)

    # Check if the number is undulating
    for i in range(1, len(n)):
        if abs(int(n[i]) - int(n[i-1])) != 1:
            return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)