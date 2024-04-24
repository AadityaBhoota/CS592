import re

def remove_lowercase(str1):
    new_str = re.sub(r'[a-z]', '', str1)
    return new_str

# Examples




def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)