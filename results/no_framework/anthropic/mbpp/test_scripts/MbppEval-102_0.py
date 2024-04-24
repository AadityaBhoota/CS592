def snake_to_camel(word):
    """
    Converts a snake case string to camel case string.

    Args:
        word (str): The snake case string to be converted.

    Returns:
        str: The camel case string.
    """
    words = word.split('_')
    camel_case = ''.join(w.capitalize() for w in words)
    return camel_case

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)