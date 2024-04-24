def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_starta_endb("aabbbb")
    assert not text_starta_endb("aabAbbbc")
    assert not text_starta_endb("accddbbjjj")

check(text_starta_endb)