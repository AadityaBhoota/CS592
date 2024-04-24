import re

def check_str(string):
    """
    Write a function to check whether the given string is starting with a vowel or not using regex.

    Examples:
    check_str("annie") == 'Valid'
    check_str("dawood") == 'Invalid'
    check_str("Else") == 'Valid'
    """
    regex = r'^[aeiouAEIOU][A-Za-z0-9_]*'
    if re.match(regex, string):
        return 'Valid'
    else:
        return 'Invalid'

def check(candidate):
    assert check_str("annie")
    assert not check_str("dawood")
    assert check_str("Else")

check(check_str)