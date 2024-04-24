def dict_depth(d):
    if not isinstance(d, dict) or len(d) == 0:
        return 0
    
    max_depth = 1
    for key, value in d.items():
        if isinstance(value, dict):
            max_depth = max(max_depth, 1 + dict_depth(value))
    
    return max_depth

# Test the function with provided examples




def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)