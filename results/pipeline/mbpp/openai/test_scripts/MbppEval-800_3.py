import re
def remove_all_spaces(text):
    text_without_spaces = re.sub(r'\s+', '', text)
    return text_without_spaces

def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
    assert remove_all_spaces('   python                     program')=='pythonprogram'

check(remove_all_spaces)