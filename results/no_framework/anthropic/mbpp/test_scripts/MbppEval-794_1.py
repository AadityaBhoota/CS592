import re

def text_starta_endb(text):
    '''
    Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.

    Examples:
    text_starta_endb("aabbbb") == ("Found a match!")
    text_starta_endb("aabAbbbc") == ("Not matched!")
    text_starta_endb("accddbbjjj") == ("Not matched!")
    '''
    pattern = r'^a.*b$'
    if re.match(pattern, text):
        return "Found a match!"
    else:
        return "Not matched!"

def check(candidate):
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabAbbbc")
    assert not text_starta_endb("accddbbjjj")

check(text_starta_endb)