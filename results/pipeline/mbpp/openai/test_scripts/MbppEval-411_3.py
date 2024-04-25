import re

def snake_to_camel(word):
    if not re.match(r'^[a-z]+(_[a-z]+)*$', word):
        return "Input word is not in snake case format"

    words = word.split('_')
    camel_case_words = [words[0].capitalize()] + [word.capitalize() for word in words[1:]]
    return ''.join(camel_case_words)

# Test the function




def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)