def text_match_zero_one(text):
    pattern = 'ab+'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_match_zero_one("ac")==False
    assert text_match_zero_one("dc")==False
    assert text_match_zero_one("abbbba")==True
    assert text_match_zero_one("dsabbbba")==True
    assert text_match_zero_one("asbbbba")==False
    assert text_match_zero_one("abaaa")==True

check(text_match_zero_one)