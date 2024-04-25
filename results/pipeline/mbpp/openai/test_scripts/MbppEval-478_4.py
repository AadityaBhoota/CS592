# Step 2: Use the re.sub() function to replace all lowercase substrings with an empty string
def remove_lowercase(str1):
    pattern = '[a-z]'
    modified_str = re.sub(pattern, '', str1)
    return modified_str

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')

check(remove_lowercase)