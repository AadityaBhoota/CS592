def dict_depth(d):
    if not isinstance(d, dict) or len(d) == 0:
        return 0
    
    depths = [dict_depth(value) for value in d.values() if isinstance(value, dict)]
    
    return 1 + max(depths, default=0)

# Test cases




def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)