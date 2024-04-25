def dict_depth(d):
    if not d:
        return 0
    
    max_depth = 0

    def calculate_depth(dictionary, depth):
        nonlocal max_depth
        if not dictionary:
            max_depth = max(max_depth, depth)
            return
        for key, value in dictionary.items():
            if isinstance(value, dict):
                calculate_depth(value, depth + 1)
                
    for key, value in d.items():
        if isinstance(value, dict):
            calculate_depth(value, 2)
            max_depth = max(max_depth, 2)

    return max_depth

def check(candidate):
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3

check(dict_depth)