def upper_ctr(string):
    """
    Counts the number of uppercase characters in a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The count of uppercase characters in the input string.
    """
    return sum(1 for char in string if char.isupper())

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)