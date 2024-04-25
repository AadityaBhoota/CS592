import re

def text_lowercase_underscore(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    result = re.search(pattern, text)
    if result:
        return 'Found a match!'
    else:
        return 'Notlake bracketed'''

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)