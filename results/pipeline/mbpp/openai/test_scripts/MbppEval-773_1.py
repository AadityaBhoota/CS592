import re
def occurance_substring(text,pattern):
    '''
    Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.

    Examples:
    occurance_substring('python programming, python language','python') == ('python', 0, 6)
    occurance_substring('python programming,programming language','programming') == ('programming', 7, 18)
    occurance_substring('python programming,programming language','language') == ('language', 31, 39)
    '''
import re

def occurrence_substring(text, pattern):
    '''
    Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
    
    Args:
    text (str): The input text to search for the pattern.
    pattern (str): The substring pattern to find in the text.
    
    Returns:
    tuple: If the pattern is found, return the pattern, start index, and end index of the first occurrence. Otherwise, return None.
    '''
    match = re.search(pattern, text)
    
    if match:
        return match.group(0), match.start(), match.end()
    else:
        return None

def check(candidate):
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
    assert occurance_substring('c++ programming, c++ language','python')==None

check(occurance_substring)