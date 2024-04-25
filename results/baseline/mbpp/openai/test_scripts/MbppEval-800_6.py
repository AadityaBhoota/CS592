def remove_all_spaces(text):
    return re.sub(r'\s+', '', text)

# Test the function with the examples




def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
    assert remove_all_spaces('   python                     program')=='pythonprogram'

check(remove_all_spaces)