def snake_to_camel(word):
    """
    Convert a snake case string to camel case string.

    Args:
        word (str): The snake case string to be converted.

    Returns:
        str: The camel case string.
    """
    # Split the snake case string into a list of words
    words = word.split('_')

    # Capitalize the first letter of each word, except the first word
    camel_case = [words[0]] + [w.capitalize() for w in words[1:]]

    # Join the words to form the camel case string
    return ''.join(camel_case)

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)