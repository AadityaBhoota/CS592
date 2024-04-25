import re

def check_str(string):
    """
    Check whether the given string is starting with a vowel or not using regex.

    Examples:
    check_str("annie") == 'Valid'
    check_str("dawood") == 'Invalid'
    check_str("Else") == 'Valid'
    """
    if re.match(r'^[aeiouAEIOU]', string):
        return 'Valid'
    else:
        return 'Invalid'

def check(candidate):
    assert check_str("annie")
    assert not check_str("dawood")
    assert check_str("Else")

check(check_str)