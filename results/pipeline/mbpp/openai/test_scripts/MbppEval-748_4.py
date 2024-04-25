import re
def capital_words_spaces(str1):
    result = ""
    
    for i in range(len(str1)):
        if str1[i].isupper() and i > 0:
            result += " "
        result += str1[i]
    
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)