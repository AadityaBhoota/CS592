def text_match_one(text):
    if re.search(r'ab+', text):
        return ('Found a match!')
    else:
        return ('Not matched!')

# Test the function with the given examples




def check(candidate):
    assert text_match_one("ac")==False
    assert text_match_one("dc")==False
    assert text_match_one("abba")==True

check(text_match_one)