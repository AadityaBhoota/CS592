import re
def remove_lowercase(str1):
    '''
    Write a function to remove lowercase substrings from a given string.

    Examples:
    remove_lowercase("PYTHon") == ('PYTH')
    remove_lowercase("FInD") == ('FID')
    remove_lowercase("STRinG") == ('STRG')
    '''
    return re.sub('[a-z]', '', str1)

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)