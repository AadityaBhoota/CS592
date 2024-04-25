def snake_to_camel(word):
    """
    Write a function to convert a snake case string to camel case string.

    Examples:
    snake_to_camel('python_program') == 'pythonProgram'
    snake_to_camel('python_language') == 'pythonLanguage'
    snake_to_camel('programming_language') == 'programmingLanguage'
    """
    camel_case_parts = []
    current_word = ''

    for char in word:
        if char == '_':
            if current_word:
                camel_case_parts.append(current_word.capitalize())
                current_word = ''
        else:
            current_word += char

    if current_word:
        camel_case_parts.append(current_word.capitalize())

    return ''.join(camel_case_parts)

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)