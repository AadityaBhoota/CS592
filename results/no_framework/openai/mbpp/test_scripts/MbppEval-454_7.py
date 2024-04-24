def text_match_wordz(text):
    pattern = r'\b\w*z\w*\b'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test the function




def check(candidate):
    assert text_match_wordz("pythonz.")==True
    assert text_match_wordz("xyz.")==True
    assert text_match_wordz("  lang  .")==False

check(text_match_wordz)