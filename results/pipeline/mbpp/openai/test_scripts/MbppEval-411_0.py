import re
def snake_to_camel(word):
    words = word.split('_')
    camel_words = [words[0].capitalize()]
    camel_words.extend([word.capitalize() for word in words[1:]])
    return ''.join(camel_words)

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)