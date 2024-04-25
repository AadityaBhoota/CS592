import re

def capital_words_spaces(str1):
    capital_pattern = r'(?<!\s)([A-Z][a-z]+)'
    words_with_capitals = re.findall(capital_pattern, str1)

    for word in words_with_capitals:
        str1 = str1.replace(word, ' ' + word)

    return str1

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)