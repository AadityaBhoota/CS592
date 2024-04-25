def dict_depth(d):
    def depth_helper(d, depth):
        if not isinstance(d, dict):
            return depth
        return max(depth_helper(val, depth + 1) for val in d.values())

    if not isinstance(d, dict):
        return "Input is not a dictionary"

    if not d:
        return 0

    max_depth = 1
    for val in d.values():
        if isinstance(val, dict):
            val_depth = depth_helper(val, 2)
            max_depth = max(max_depth, val_depth)

    return max_depth

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)