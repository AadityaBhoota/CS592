import re

def text_starta_endb(text):
    pattern = 'a.*b'
    return 'Found a match!' if re.match(pattern, text) else 'Not matched!'

def check(candidate):
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabAbbbc")
    assert not text_starta_endb("accddbbjjj")

check(text_starta_endb)