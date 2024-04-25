def snake_to_camel(word):
    camel_case = ""
    words = word.split('_')
    camel_case += words[0]
    for w in words[1:]:
        camel_case += w.capitalize()
    return camel_case

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)