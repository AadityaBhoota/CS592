import re

def occurance_substring(text, pattern):
    """
    Find the occurrence and position of the substrings within a string.
    
    Return a tuple containing the matched substring, start index, and end index.
    Return None if there is no match.
    """
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)