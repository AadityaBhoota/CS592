def snake_to_camel(word):
    words = word.split('_')
    capitalized_words = [w.capitalize() for w in words]
    camel_case = ''.join(capitalized_words)
    return camel_case

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)