import re

def snake_to_camel(word):
    """
    Write a function to convert the given snake case string to camel case string.

    Examples:
    snake_to_camel('android_tv') == 'AndroidTv'
    snake_to_camel('google_pixel') == 'GooglePixel'
    snake_to_camel('apple_watch') == 'AppleWatch'
    """
    words = word.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)