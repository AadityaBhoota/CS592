import re

def snake_to_camel(word):
    '''
    Converts a snake case string to camel case.

    Examples:
    snake_to_camel('android_tv') == 'AndroidTv'
    snake_to_camel('google_pixel') == 'GooglePixel'
    snake_to_camel('apple_watch') == 'AppleWatch'
    '''
    # Split the snake case string into a list of words
    words = word.split('_')

    # Capitalize the first letter of each word, except the first word
    camel_case = [words[0]] + [w.capitalize() for w in words[1:]]

    # Join the words into a single string
    return ''.join(camel_case)

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)