import re

def capital_words_spaces(str1):
    '''
    Write a function to put spaces between words starting with capital letters in a given string.

    Examples:
    capital_words_spaces("Python") == 'Python'
    capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
    '''
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', str1)

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)