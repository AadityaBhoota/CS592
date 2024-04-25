import re

def text_match_three(text):
    ''' text_match_three takes in a string and returns a tuple based on if the pattern 'ab{3}' is found '''
    match = re.search(r'ab{3}', text)
    if match:
        return ('Found a match!')
    else:
        return ('Not matched!')

def check(candidate):
    assert not text_match_three("ac")
    assert not text_match_three("dc")
    assert text_match_three("abbbba")
    assert text_match_three("caacabbbba")

check(text_match_three)