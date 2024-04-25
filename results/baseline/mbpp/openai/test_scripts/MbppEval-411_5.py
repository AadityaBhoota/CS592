def snake_to_camel(word):
    parts = word.split('_')
    camel_word = parts[0].capitalize() + ''.join([part.capitalize() for part in parts[1:]])
    return camel_word

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)