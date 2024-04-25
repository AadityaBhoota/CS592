def snake_to_camel(word):
    """
    Convert a snake case string to camel case string.

    Examples:
    snake_to_camel('python_program') == 'PythonProgram'
    snake_to_camel('python_language') == 'PythonLanguage'
    snake_to_camel('programming_language') == 'ProgrammingLanguage'
    """
    words = word.split('_')
    return ''.join(w.capitalize() for w in words)

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)