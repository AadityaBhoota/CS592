import re

def text_match_three(text):
    if re.search(r'ab{3}', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test the function




def check(candidate):
    assert not text_match_three("ac")
    assert not text_match_three("dc")
    assert text_match_three("abbbba")
    assert text_match_three("caacabbbba")

check(text_match_three)