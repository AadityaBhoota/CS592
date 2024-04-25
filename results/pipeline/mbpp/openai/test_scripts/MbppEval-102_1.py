def snake_to_camel(word):
    words = word.split('_')
    # Convert all words in the list to lowercase
    words = [w.lower() for w in words]

    # Capitalize the first letter of each word after the first word
    camel_words = [words[0]]
    camel_words.extend([w.capitalize() for w in words[1:]])

    return ''.join(camel_words)

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)