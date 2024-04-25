def number_ctr(string):
    """
    Count the number of digits in a given string.

    Args:
        string (str): The input string to count the digits in.

    Returns:
        int: The count of digits in the input string.
    """
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

def check(candidate):
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') == 1
    assert number_ctr('123') == 3
    assert number_ctr('3wond-1ers2') == 3

check(number_ctr)