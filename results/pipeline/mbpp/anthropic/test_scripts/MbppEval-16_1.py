import re

def text_lowercase_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    if re.search(pattern, text):
        return True
    else:
        return False

def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)