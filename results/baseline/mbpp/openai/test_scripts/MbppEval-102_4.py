def snake_to_camel(word):
    parts = word.split('_')
    camel_case_word = parts[0].capitalize() + ''.join([part.capitalize() for part in parts[1:]])
    return camel_case_word

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)