def snake_to_camel(word):
    camel_case = ''
    words = word.split('_')
    camel_case += words[0]
    for w in words[1:]:
        camel_case += w.capitalize()
    return camel_case

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)