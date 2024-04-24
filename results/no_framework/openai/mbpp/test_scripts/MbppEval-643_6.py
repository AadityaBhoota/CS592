def text_match_wordz_middle(text):
    # regex pattern to match 'z' in the middle of a word
    pattern = r'\b\w*z\w*\b'
    
    # check if the pattern is found in the text
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test cases




def check(candidate):
    assert text_match_wordz_middle("pythonzabc.")==True
    assert text_match_wordz_middle("zxyabc.")==False
    assert text_match_wordz_middle("  lang  .")==False

check(text_match_wordz_middle)