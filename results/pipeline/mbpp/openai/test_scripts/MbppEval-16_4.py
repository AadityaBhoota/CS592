import re

def text_lowercase_underscore(text):
    match = re.search(r'\b[a-z]+_[a-z]+\b', text)
    if match:
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)