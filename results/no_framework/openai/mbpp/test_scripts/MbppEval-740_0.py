def tuple_to_dict(test_tup):
    # Create an empty dictionary to store the key-value pairs
    result_dict = {}
    
    # Check if the tuple has an even number of elements
    if len(test_tup) % 2 != 0:
        raise ValueError("Input tuple must have an even number of elements")
    
    # Iterate over the tuple in steps of 2 to extract key-value pairs
    for i in range(0, len(test_tup), 2):
        key = test_tup[i]
        value = test_tup[i + 1]
        result_dict[key] = value
    
    return result_dict

# Test cases




def check(candidate):
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}

check(tuple_to_dict)