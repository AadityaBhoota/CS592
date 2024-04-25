import re

def text_match_one(text):
    '''
    Matches a string that has an 'a' followed by one or more 'b's.

    Args:
    text (str): Input string to check for the pattern.

    Returns:
    str: 'Found a match!' if pattern found, 'Not matched!' otherwise.
    '''
    if re.search(r'ab+', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_match_one("ac")==False
    assert text_match_one("dc")==False
    assert text_match_one("abba")==True

check(text_match_one)