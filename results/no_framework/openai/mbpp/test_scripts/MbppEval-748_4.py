    # Using regular expression to split the string at the capital letters and then join it with spaces
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', str1)
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)