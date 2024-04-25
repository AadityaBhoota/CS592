import re
def capital_words_spaces(str1):
    output_str = ""
    
    for i in range(len(str1)):
        if str1[i].isupper() and i != 0:
            output_str += " "
        
        output_str += str1[i]

    return output_str

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)