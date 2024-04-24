import re

def text_match_wordz(text):
    '''
    Write a function that matches a word containing 'z'.

    Examples:
    text_match_wordz("pythonz.") == ('Found a match!')
    text_match_wordz("xyz.") == ('Found a match!')
    text_match_wordz("  lang  .") == ('Not matched!')
    '''
    pattern = r'\b\w*z\w*\b'
    if re.search(pattern, text):
        return ('Found a match!')
    else:
        return ('Not matched!')

def check(candidate):
    assert text_match_wordz("pythonz.")==True
    assert text_match_wordz("xyz.")==True
    assert text_match_wordz("  lang  .")==False

check(text_match_wordz)