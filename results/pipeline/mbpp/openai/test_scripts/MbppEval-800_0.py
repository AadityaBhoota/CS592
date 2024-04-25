import re

def remove_all_spaces(text):
    if not isinstance(text, str):
        return "Input is not a string"
    else:
        return re.sub(r'\s+', '', text)

def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
    assert remove_all_spaces('   python                     program')=='pythonprogram'

check(remove_all_spaces)