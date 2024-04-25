import re

def snake_to_camel(word):
    """
    Convert a snake case string to camel case.

    Args:
        word (str): The snake case string to be converted.

    Returns:
        str: The equivalent camel case string.
    """
    # Split the snake case string on the '_' character
    words = word.split('_')

    # Capitalize the first character of each word, except the first one
    camel_case = [words[0]] + [w.capitalize() for w in words[1:]]

    # Join the capitalized words to form the camel case string
    return ''.join(camel_case)

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)