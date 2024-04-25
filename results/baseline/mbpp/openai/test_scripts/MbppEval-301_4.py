def dict_depth(d):
    if isinstance(d, dict):
        if d:
            return 1 + max(dict_depth(v) for k, v in d.items())
        else:
            return 1
    else:
        return 0

# Test cases




def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)