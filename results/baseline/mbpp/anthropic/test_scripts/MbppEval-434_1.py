import re

def text_match_one(text):
    '''
    Write a function that matches a string that has an a followed by one or more b's.

    Examples:
    text_match_one("ac") == ('Not matched!')
    text_match_one("dc") == ('Not matched!')
    text_match_one("abba") == ('Found a match!')
    '''
    pattern = r'ab+'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_match_one("ac")==False
    assert text_match_one("dc")==False
    assert text_match_one("abba")==True

check(text_match_one)