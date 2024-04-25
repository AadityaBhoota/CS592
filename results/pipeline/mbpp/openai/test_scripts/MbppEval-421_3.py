def concatenate_tuple(test_tup):
    result = ""
    for element in test_tup:
        result += str(element) + '-'
    result = result[:-1]  # Remove the last '-' from the result string
    return result

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)