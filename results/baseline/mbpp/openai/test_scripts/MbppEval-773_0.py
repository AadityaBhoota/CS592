import re
def occurance_substring(text,pattern):
    '''
    Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.

    Examples:
    occurance_substring('python programming, python language','python') == ('python', 0, 6)
    occurance_substring('python programming,programming language','programming') == ('programming', 7, 18)
    occurance_substring('python programming,programming language','language') == ('language', 31, 39)
    '''
def occurrence_substring(text, pattern):
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None

# Testing the function with given examples



def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)