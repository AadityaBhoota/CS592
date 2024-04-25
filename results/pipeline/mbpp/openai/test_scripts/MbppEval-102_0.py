def snake_to_camel(word):
    words = word.split('_')
    camel_case_words = [words[0].capitalize()] + [word.capitalize() for word in words[1:]]
    return ''.join(camel_case_words)

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)