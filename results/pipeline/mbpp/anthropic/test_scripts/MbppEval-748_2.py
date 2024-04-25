import re

def capital_words_spaces(str1):
    result = ""
    for i, char in enumerate(str1):
        if i > 0 and char.isupper() and str1[i-1] != " ":
            result += " "
        result += char
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)