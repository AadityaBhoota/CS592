def extract_rear(test_tuple):
    return [s[-1] for s in test_tuple]

# Test cases




def check(candidate):
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

check(extract_rear)