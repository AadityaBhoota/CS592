def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    return 1 + max(dict_depth(d[k]) for k in d)

# Test the function with examples




def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)