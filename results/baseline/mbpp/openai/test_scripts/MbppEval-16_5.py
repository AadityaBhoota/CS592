import re

def text_lowercase_underscore(text):
    # Define the regex pattern to match lowercase letters joined with an underscore
    pattern = r'\b[a-z]+_[a-z]+\b'

    # Search for the pattern in the input text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("aab_Abbbc")==(False)
    assert text_lowercase_underscore("Aaab_abbbc")==(False)

check(text_lowercase_underscore)