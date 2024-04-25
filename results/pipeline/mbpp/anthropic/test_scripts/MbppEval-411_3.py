import re

def snake_to_camel(word):
    words = word.split('_')
    camel_case_words = [words[0]]
    for w in words[1:]:
        camel_case_words.append(w.capitalize())
    camel_case = ''.join(camel_case_words)
    return camel_case

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)