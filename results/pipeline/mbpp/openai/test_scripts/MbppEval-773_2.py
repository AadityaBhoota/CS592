import re

def occurance_substring(text, pattern):
    match = re.search(pattern, text)
    if match:
        pattern_match = match.group()
        start_index = match.start()
        end_index = match.end() - 1
        return pattern_match, start_index, end_index
    else:
        return None

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)