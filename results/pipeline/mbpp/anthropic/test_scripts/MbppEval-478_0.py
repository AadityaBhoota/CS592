def remove_lowercase(str1):
    result = ""
    for char in str1:
        if char.isupper():
            result += char
    return result

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)