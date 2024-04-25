import re

def text_match_wordz_middle(text):
    return re.search(r'\Bz\B', text) is not None and 'Found a match!' or 'Not matched!'

def check(candidate):
    assert text_match_wordz_middle("pythonzabc.")==True
    assert text_match_wordz_middle("zxyabc.")==False
    assert text_match_wordz_middle("  lang  .")==False

check(text_match_wordz_middle)