import re

regex = r'^[a-z]$|^([a-z]).*\1$'

def check_char(string):
    return "Valid" if re.match(regex, string) else "Invalid"

def check(candidate):
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"

check(check_char)