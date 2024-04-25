import re

def snake_to_camel(word):
    result = ""
    words = word.split("_")
    
    # Convert the first word to start with uppercase
    result += words[0].capitalize()
    
    # Convert the remaining words to start with uppercase
    for w in words[1:]:
        result += w.capitalize()
    
    return result

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)