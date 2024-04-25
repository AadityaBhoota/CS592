def dict_depth(d, depth=1):
    if isinstance(d, dict):
        max_depth = 0
        for value in d.values():
            if isinstance(value, dict):
                max_depth = max(max_depth, dict_depth(value, depth + 1))
        return max_depth + depth
    return depth

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)