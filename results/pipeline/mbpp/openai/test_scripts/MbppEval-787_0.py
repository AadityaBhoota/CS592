import re

def text_match_three(text):
    pattern = "ab{3}"
    result = re.search(pattern, text)
    if result:
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert not text_match_three("ac")
    assert not text_match_three("dc")
    assert text_match_three("abbbba")
    assert text_match_three("caacabbbba")

check(text_match_three)