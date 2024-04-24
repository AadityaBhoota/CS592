def find_char_long(text):
    pattern = r'\b\w{4,}\b'
    return re.findall(pattern, text)

# Test the function



def check(candidate):
    assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
    assert set(find_char_long('Jing Eco and Tech')) == set(['Jing', 'Tech'])
    assert set(find_char_long('Jhingai wulu road Zone 3')) == set(['Jhingai', 'wulu', 'road', 'Zone'])

check(find_char_long)