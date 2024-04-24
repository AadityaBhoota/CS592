import re

def text_match_two_three(text):
    if re.search(r'ab{2,3}', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_match_two_three("ac")==(False)
    assert text_match_two_three("dc")==(False)
    assert text_match_two_three("abbbba")==(True)

check(text_match_two_three)