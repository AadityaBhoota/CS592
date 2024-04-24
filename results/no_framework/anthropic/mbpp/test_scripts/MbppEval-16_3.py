import re

def text_lowercase_underscore(text):
    '''
    Write a function to that returns "Found a match!" if the input string contains sequences of lowercase letters joined with an underscore, and "Not matched!" otherwise.

    Examples:
    text_lowercase_underscore("aab_cbbbc") == "Found a match!"
    text_lowercase_underscore("aab_Abbbc") == "Not matched!"
    text_lowercase_underscore("Aaab_abbbc") == "Not matched!"
    '''
    if re.search(r'^[a-z]+(?:_[a-z]+)*$', text):
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)