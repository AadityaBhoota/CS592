import re

def text_match_one(text):
    # Define the pattern to match a string that has an 'a' followed by one or more 'b's
    pattern = 'ab+'
    
    # Check if the pattern matches the given text
    if re.search(pattern, text):
        return ('Found a match!')
    else:
        return ('Not matched!')

def check(candidate):
    assert text_match_one("ac")==False
    assert text_match_one("dc")==False
    assert text_match_one("abba")==True

check(text_match_one)