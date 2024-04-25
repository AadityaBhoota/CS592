def dict_depth(d, depth=1):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth + 1) for v in d.values())

# Test cases




def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)