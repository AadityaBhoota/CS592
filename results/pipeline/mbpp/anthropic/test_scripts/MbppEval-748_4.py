import re

def capital_words_spaces(str1):
    result = ""
    prev_char_space = True # Assume the first character is preceded by a space
    
    for char in str1:
        if char.isupper() and not prev_char_space:
            result += " "
        result += char
        prev_char_space = char == " "
    
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)