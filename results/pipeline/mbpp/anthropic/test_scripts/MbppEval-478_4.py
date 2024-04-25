import re

def remove_lowercase(str1):
    pattern = r'[a-z]+'
    result = re.sub(pattern, '', str1)
    return result

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)