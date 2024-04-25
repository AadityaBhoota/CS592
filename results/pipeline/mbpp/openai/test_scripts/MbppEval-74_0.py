def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False
    
    mapping = {}
    
    for color, pattern in zip(colors, patterns):
        if color in mapping:
            if mapping[color] != pattern:
                return False
        else:
            if pattern in mapping.values():
                return False
            mapping[color] = pattern
    
    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)