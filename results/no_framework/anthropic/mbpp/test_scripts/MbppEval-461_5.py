def upper_ctr(string):
    """
    Write a python function to count the upper case characters in a given string.

    Examples:
    upper_ctr('PYthon') == 1
    upper_ctr('BigData') == 2
    upper_ctr('program') == 0
    """
    count = 0
    for char in string:
        if char.isupper():
            count += 1
    return count

def check(candidate):
    assert upper_ctr('PYthon') == 1
    assert upper_ctr('BigData') == 1
    assert upper_ctr('program') == 0

check(upper_ctr)