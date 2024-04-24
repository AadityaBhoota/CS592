import re
def capital_words_spaces(str1):
    words = re.findall('[A-Z][a-z]*', str1)
    return ' '.join(words)

# Test cases




def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)