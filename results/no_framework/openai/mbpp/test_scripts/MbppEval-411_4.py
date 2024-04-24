import re

def snake_to_camel(word):
    words = word.split('_')
    return ''.join([w.capitalize() for w in words])

# Test the function




def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)