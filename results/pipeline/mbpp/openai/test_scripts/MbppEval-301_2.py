def dict_depth(d):
    depth = 0
    
    if not d:
        return 0
    
    max_depth = 0
    
    if not isinstance(d, dict):
        return depth
    
    for key, value in d.items():
        if isinstance(value, dict):
            curr_depth = dict_depth(value)
            max_depth = max(max_depth, curr_depth + 1)
    
    return max_depth

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)