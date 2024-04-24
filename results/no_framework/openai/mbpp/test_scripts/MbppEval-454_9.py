import re

def text_match_wordz(text):
    pattern = r'\b\w*z\w*\b'  # Word containing 'z'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test the function with the examples from the docstring




def check(candidate):
    assert text_match_wordz("pythonz.")==True
    assert text_match_wordz("xyz.")==True
    assert text_match_wordz("  lang  .")==False

check(text_match_wordz)