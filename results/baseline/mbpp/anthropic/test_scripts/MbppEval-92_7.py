def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    Args:
        n (str): The input number as a string.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    # Convert the input string to a list of digits
    digits = [int(d) for d in str(n)]

    # Check if the number is undulating
    expected_pattern = [1, 0, 1, 0, 1, 0]
    for i in range(len(digits) - 5):
        if digits[i:i+6] != expected_pattern:
            return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)