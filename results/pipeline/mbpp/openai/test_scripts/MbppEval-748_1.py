import re

def capital_words_spaces(str1):
    # Initializing an empty list to store words
    words = []
    
    # Starting with an empty string 'current_word'
    current_word = ""
    
    # Step 2: Iterate over each character in the input string
    for char in str1:
        # Step 3: Check if the current character is uppercase
        if char.isupper():
            # Step 4: Add the current_word to the list and start a new current_word
            if current_word:
                words.append(current_word)
            current_word = char
        else:
            current_word += char  # Append the character to the current_word

    # Append the last current_word to the list
    words.append(current_word)

    return ' '.join(words)

def check(candidate):
    assert capital_words_spaces("Python") == 'Python'
    assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
    assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'

check(capital_words_spaces)