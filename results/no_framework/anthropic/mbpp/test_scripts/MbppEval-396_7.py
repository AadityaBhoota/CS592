import re

regex = r'^[a-z]$|^([a-z]).*\1$'

def check_char(string):
    """
    Write a function to check whether the given string starts and ends with the same character or not.

    Examples:
    check_char("abba") == "Valid"
    check_char("a") == "Valid"
    check_char("abcd") == "Invalid"
    """
    if re.match(regex, string):
        return "Valid"
    else:
        return "Invalid"

def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"

check(check_char)