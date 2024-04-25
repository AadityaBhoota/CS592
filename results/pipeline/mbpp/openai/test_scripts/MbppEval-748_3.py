import re
def capital_words_spaces(str1):
    result = ""
    for char in str1:
        if char.isupper():
            if result and result[-1] != " ":
                result += " "
            result += char
        else:
            result += char
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)