def occurance_substring(text, pattern):
    matches = re.finditer(pattern, text)
    result = []
    for match in matches:
        result.append((match.group(), match.start(), match.end()-1))
    if len(result) == 0:
        return None
    else:
        return result[0]  # Returning the first match only

# Test cases



def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)