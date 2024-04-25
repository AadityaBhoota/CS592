import re

def text_match_two_three(text):
    pattern = r'ab{2,3}$'
    if re.search(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert text_match_two_three("ac")==(False)
    assert text_match_two_three("dc")==(False)
    assert text_match_two_three("abbbba")==(True)

check(text_match_two_three)