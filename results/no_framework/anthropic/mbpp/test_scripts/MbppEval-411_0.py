import re

def snake_to_camel(word):
    '''
    Write a function to convert the given snake case string to camel case string.

    Examples:
    snake_to_camel('android_tv') == 'AndroidTv'
    snake_to_camel('google_pixel') == 'GooglePixel'
    snake_to_camel('apple_watch') == 'AppleWatch'
    '''
    # Split the snake case string on '_'
    words = word.split('_')
    
    # Capitalize the first letter of each word, except the first one
    camel_case = [words[0]] + [w.capitalize() for w in words[1:]]
    
    # Join the capitalized words
    return ''.join(camel_case)

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)