def concatenate_tuple(test_tup, delimiter='-'):
    concatenated_str = ''
    
    for element in test_tup:
        concatenated_str += str(element) + delimiter

    return concatenated_str[:-len(delimiter)]

# Test the function with the given examples




def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)