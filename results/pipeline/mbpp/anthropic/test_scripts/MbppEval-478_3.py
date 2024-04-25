import re

def remove_lowercase(str1):
    pattern = r'[a-z]+'
    return re.sub(pattern, '', str1)

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)