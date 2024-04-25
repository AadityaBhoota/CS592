def extract_rear(test_tuple):
    rear_elements = []
    
    for string in test_tuple:
        rear_index_element = string[-1]
        rear_elements.append(rear_index_element)
    
    return rear_elements

def check(candidate):
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']

check(extract_rear)