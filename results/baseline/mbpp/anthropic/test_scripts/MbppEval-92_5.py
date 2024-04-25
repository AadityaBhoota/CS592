def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    An undulating number is a number where the digits alternate between increasing and decreasing.

    Args:
        n (str): The number to be checked.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    n = str(n)
    if len(n) < 2:
        return False

    is_increasing = None
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            return False
        elif n[i] > n[i-1]:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                return False
        else:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)