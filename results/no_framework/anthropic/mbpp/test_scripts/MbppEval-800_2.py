import re

def remove_all_spaces(text):
    """
    Write a function to remove all whitespaces from a string.

    Examples:
    remove_all_spaces('python  program') == 'pythonprogram'
    remove_all_spaces('python   programming    language') == 'pythonprogramminglanguage'
    remove_all_spaces('python                     program') == 'pythonprogram'
    """
    return re.sub(r'\s+', '', text)

def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
    assert remove_all_spaces('   python                     program')=='pythonprogram'

check(remove_all_spaces)