def snake_to_camel(word):
    words = word.split('_')
    words = [w.lower() for w in words]
    
    # Capitalize the first letter of each word except the first word
    camel_words = [words[0]] + [w.capitalize() for w in words[1:]]
    
    # Concatenate the capitalized words
    camel_case = ''.join(camel_words)
    
    return camel_case

def check(candidate):
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'

check(snake_to_camel)