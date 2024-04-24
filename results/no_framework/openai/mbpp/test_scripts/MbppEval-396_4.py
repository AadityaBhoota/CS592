import re

regex = r'^([a-z]).*\1$'

def check_char(string):
    if re.match(regex, string):
        return "Valid"
    else:
        return "Invalid"

# Test examples




def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"

check(check_char)