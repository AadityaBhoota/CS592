import re

def text_starta_endb(text):
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabAbbbc")
    assert not text_starta_endb("accddbbjjj")

check(text_starta_endb)