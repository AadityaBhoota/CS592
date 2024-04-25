import re

def find_char_long(text):
    '''
    Write a function to find all words which are at least 4 characters long in a string.

    Examples:
    find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']
    find_char_long('Jing Eco and Tech') == ['Jing', 'Tech']
    find_char_long('Jhingai wulu road Zone 3') == ['Jhingai', 'wulu', 'road', 'Zone']
    '''
    words = re.findall(r'\b\w{4,}\b', text)
    return words

def check(candidate):
    assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
    assert set(find_char_long('Jing Eco and Tech')) == set(['Jing', 'Tech'])
    assert set(find_char_long('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])

check(find_char_long)