def concatenate_tuple(test_tup):
    concatenated_str = ''
    delimiter = '-'
    
    for element in test_tup:
        concatenated_str += str(element) + delimiter
    
    concatenated_str = concatenated_str[:-1]  # Remove the last delimiter
    
    return concatenated_str

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)