import re

def snake_to_camel(word):
    """
    Converts a snake case string to camel case.
    
    Args:
        word (str): The snake case string to be converted.
    
    Returns:
        str: The camel case version of the input string.
    """
    # Split the snake case string into words
    words = word.split('_')
    
    # Capitalize the first letter of each word, except the first word
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    # Join the capitalized words into a single string
    camel_case_string = ''.join(camel_case_words)
    
    return camel_case_string

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)