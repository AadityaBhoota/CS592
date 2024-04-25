import re

def check_char(string):
    if re.match(r'^[a-z]$|^([a-z]).*\1$', string):
        return "Valid"
    else:
        return "Invalid"

def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"

check(check_char)