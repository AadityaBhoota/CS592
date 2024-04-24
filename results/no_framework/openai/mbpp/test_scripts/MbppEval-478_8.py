def remove_lowercase(str1):
    return re.sub(r'[a-z]', '', str1)

# Test cases




def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)