def dict_depth(d):
    """
    Write a function to find the depth of a dictionary.

    Examples:
    dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
    dict_depth({'a':1, 'b': {'c':'python'}}) == 2
    dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}}) == 3
    """

    def get_depth(d):
        if not d:
            return 1
        return 1 + (max(map(get_depth, d.values())) if d else 0)

    return get_depth(d)

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)