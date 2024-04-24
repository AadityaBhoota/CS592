def is_undulating(n):
    """
    Check whether the given number is undulating or not.

    Examples:
    is_undulating("1212121") == True
    is_undulating("1991") == False
    is_undulating("121") == True
    """
    # Convert the input to a string
    n_str = str(n)

    # Check if the length of the string is less than 3
    if len(n_str) < 3:
        return True

    # Check if the digits are alternating
    for i in range(1, len(n_str), 2):
        if n_str[i] == n_str[i-1]:
            return False

    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)