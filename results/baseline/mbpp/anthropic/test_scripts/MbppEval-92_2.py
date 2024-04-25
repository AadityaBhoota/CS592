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

    # Convert the input string to a list of integers
    digits = [int(d) for d in n]

    # Check if the difference between consecutive digits alternates between 1 and -1
    diff = [digits[i] - digits[i-1] for i in range(1, len(digits))]
    return all(d in (1, -1) for d in diff)

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)