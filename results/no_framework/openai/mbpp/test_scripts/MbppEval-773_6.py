def occurance_substring(text, pattern):
    match = re.search(pattern, text)
    if match:
        return (match.group(0), match.start(), match.end() - 1)
    else:
        return None

# Test the function
assert occurance_substring('python programming, python language','python') == ('python', 0, 5)
assert occurance_substring('python programming,programming language','programming') == ('programming', 7, 16)
assert occurance_substring('python programming,programming language','language') == ('language', 31, 38)


def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)