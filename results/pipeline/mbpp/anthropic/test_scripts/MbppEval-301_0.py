def dict_depth(d):
    """
    Write a function to find the depth of a dictionary.

    Examples:
    dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
    dict_depth({'a':1, 'b': {'c':'python'}}) == 2
    dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}}) == 3
    """
    return _dict_depth(d, 1)

def _dict_depth(d, depth):
    if not d:
        return depth
    
    max_depth = depth
    for value in d.values():
        if isinstance(value, dict):
            max_depth = max(max_depth, _dict_depth(value, depth + 1))
    
    return max_depth

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)