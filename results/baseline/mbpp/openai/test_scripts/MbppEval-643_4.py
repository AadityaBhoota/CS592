import re
def text_match_wordz_middle(text):
    '''
    Write a function that checks if a strings contains 'z', except at the start and end of the word.

    Examples:
    text_match_wordz_middle("pythonzabc.") == ('Found a match!')
    text_match_wordz_middle("xyzabc.") == ('Found a match!')
    text_match_wordz_middle("  lang  .") == ('Not matched!')
    '''
    # Check if 'z' is surrounded by any word character on both sides
    if re.search(r'\b\wz\w\b', text):
        return 'Found a match!'
    else:
        return 'Not matched!'

def check(candidate):
    assert text_match_wordz_middle("pythonzabc.")==True
    assert text_match_wordz_middle("zxyabc.")==False
    assert text_match_wordz_middle("  lang  .")==False

check(text_match_wordz_middle)