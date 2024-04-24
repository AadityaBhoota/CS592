import re

def text_match_three(text):
    pattern = r'a(bbb)'
    match = re.search(pattern, text)
    if match:
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert not text_match_three("ac")
    assert not text_match_three("dc")
    assert text_match_three("abbbba")
    assert text_match_three("caacabbbba")

check(text_match_three)