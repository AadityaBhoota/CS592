import re

def occurance_substring(text, pattern):
    matches = re.finditer(pattern, text)
    match = next(matches, None)  # Get the first match or None if no match
    if match:
        substring = match.group()
        start = match.start()
        end = match.end()
        return (substring, start, end)
    return None

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)