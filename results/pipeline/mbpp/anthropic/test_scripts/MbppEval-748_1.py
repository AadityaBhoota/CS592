def capital_words_spaces(str1):
    words = str1.split()
    result = []
    for word in words:
        if word[0].isupper():
            result.append(' ' + word)
        else:
            result.append(word)
    return ''.join(result).strip()

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)