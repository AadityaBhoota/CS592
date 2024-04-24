import re

def snake_to_camel(word):
    words = word.split('_')
    camel_word = words[0].capitalize() + ''.join([w.capitalize() for w in words[1:]])
    return camel_word

# Test cases




def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)