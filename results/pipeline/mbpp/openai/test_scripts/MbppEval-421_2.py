def concatenate_tuple(test_tup):
    result = ""
    
    for idx, val in enumerate(test_tup):
        if idx != 0:
            result += '-' + str(val)
        else:
            result += str(val)
    
    return result

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)