def is_undulating(n):
    """
    Checks whether the given number is undulating or not.

    Args:
        n (str): The input number as a string.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    if len(n) < 2:
        return False

    # Convert the input string to a list of digits
    digits = [int(digit) for digit in n]

    # Check if the digits form an undulating pattern
    for i in range(1, len(digits)):
        if digits[i] == digits[i-1]:
            return False
        if i > 1 and (digits[i] - digits[i-1]) * (digits[i-1] - digits[i-2]) < 0:
            return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)