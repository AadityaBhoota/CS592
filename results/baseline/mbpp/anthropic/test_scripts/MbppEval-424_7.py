def extract_rear(test_tuple):
    """
    Write a function to extract only the rear index element of each string in the given tuple.

    Examples:
    extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
    extract_rear(('Avenge', 'for', 'People')) == ['e', 'r', 'e']
    extract_rear(('Gotta', 'get', 'go')) == ['a', 't', 'o']
    """
    return [string[-1] for string in test_tuple]

def check(candidate):
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

check(extract_rear)