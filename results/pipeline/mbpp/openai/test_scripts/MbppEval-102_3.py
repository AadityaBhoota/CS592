def snake_to_camel(word):
    words = word.split('_')
    
    # Capitalize the first letter of each word except for the first word
    camel_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    # Step 3: Join the words back together to form the camel case string
    camel_case_string = ''.join(camel_words)
    
    return camel_case_string

# Test the function with examples




def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')

check(snake_to_camel)