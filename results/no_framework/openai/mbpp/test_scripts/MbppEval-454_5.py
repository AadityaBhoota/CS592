import re
def text_match_wordz(text):
    # define the pattern to search for a word containing 'z'
    pattern = r'\b\w*z\w*\b'  # word that contains 'z'

    # search for the pattern in the given text
    match = re.search(pattern, text)

    if match:
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test the function with examples




def check(candidate):
    assert text_match_wordz("pythonz.")==True
    assert text_match_wordz("xyz.")==True
    assert text_match_wordz("  lang  .")==False

check(text_match_wordz)