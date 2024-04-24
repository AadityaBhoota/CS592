import re

def text_match_zero_one(text):
    """
    Write a function that matches a string that has an 'a' followed by one or more 'b's.
    Examples:
    text_match_zero_one("ac") == ('Not matched!')
    text_match_zero_one("dc") == ('Not matched!')
    text_match_zero_one("abbbba") == ('Found a match!')
    """
    pattern = r"a(b+)"
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert text_match_zero_one("ac")==False
    assert text_match_zero_one("dc")==False
    assert text_match_zero_one("abbbba")==True
    assert text_match_zero_one("dsabbbba")==True
    assert text_match_zero_one("asbbbba")==False
    assert text_match_zero_one("abaaa")==True

check(text_match_zero_one)