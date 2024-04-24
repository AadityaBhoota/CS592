def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    mapping = {}
    
    for color, pattern in zip(colors, patterns):
        if color not in mapping:
            mapping[color] = pattern
        elif mapping[color] != pattern:
            return False
    
    return True

# Test cases




def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)