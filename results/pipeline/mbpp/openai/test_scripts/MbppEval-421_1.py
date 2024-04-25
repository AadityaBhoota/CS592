def concatenate_tuple(test_tup):
    result = ""
    
    for i in range(len(test_tup)):
        element = str(test_tup[i])  # Convert each element to a string
        result += element  # Concatenate the element to the result
        
        if i != len(test_tup) - 1:
            result += '-'  # Append the delimiter '-' after each element except the last element

    return result

def check(candidate):
    assert concatenate_tuple(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'

check(concatenate_tuple)