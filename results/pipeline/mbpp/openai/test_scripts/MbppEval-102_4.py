def snake_to_camel(word):
    words = word.split('_')
    camel_words = [words[0]] + [word.capitalize() for word in words[1:]]
    camel_case_word = ''.join(camel_words)
    return camel_case_word

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)