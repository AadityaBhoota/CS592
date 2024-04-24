import re

def capital_words_spaces(str1):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", str1)

# Test cases




def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)