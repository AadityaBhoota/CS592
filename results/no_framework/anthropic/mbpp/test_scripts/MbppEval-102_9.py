def snake_to_camel(word):
    """
    Convert a snake case string to camel case.

    Args:
        word (str): The snake case string to be converted.

    Returns:
        str: The converted camel case string.
    """
    # Split the snake case string into a list of words
    words = word.split('_')

    # Capitalize the first letter of each word, except the first one
    camel_case_words = [words[0]] + [w.capitalize() for w in words[1:]]

    # Join the words into a camel case string
    camel_case_word = ''.join(camel_case_words)

    return camel_case_word

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)