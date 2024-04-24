def snake_to_camel(word):
    """
    Convert a snake case string to camel case.

    Args:
        word (str): The input snake case string.

    Returns:
        str: The converted camel case string.
    """
    words = word.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)