import re

def capital_words_spaces(str1):
    """
    Write a function to put spaces between words starting with capital letters in a given string.

    Examples:
    capital_words_spaces("Python") == 'Python'
    capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
    """
    # Use a regular expression to find the capitalized words
    pattern = r'[A-Z][a-z]*'
    matches = re.findall(pattern, str1)

    # Join the matches with spaces
    result = ' '.join(matches)
    return result

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)