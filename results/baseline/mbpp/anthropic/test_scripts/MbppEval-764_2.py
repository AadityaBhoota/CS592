def number_ctr(string):
    """
    Write a python function to count the number of digits in a given string.

    Examples:
    number_ctr('program2bedone') == 1
    number_ctr('3wonders') == 1
    number_ctr('123') == 3
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