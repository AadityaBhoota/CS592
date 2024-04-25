import re

def remove_lowercase(str1):
    lowercase_substrings = re.findall(r'[a-z]+', str1)
    new_string = ''.join(char for char in str1 if char not in ''.join(lowercase_substrings))
    return new_string

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)