import re

def check_char(string):
    pattern = r'^([a-z]).*\1$'
    if re.match(pattern, string):
        return "Valid"
    else:
        return "Invalid"

# Test cases




def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"

check(check_char)