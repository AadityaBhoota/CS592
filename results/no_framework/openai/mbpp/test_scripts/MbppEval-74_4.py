def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False
    
    pattern_map = {}
    used_patterns = set()
    
    for color, pattern in zip(colors, patterns):
        if color not in pattern_map:
            if pattern in used_patterns:
                return False
            pattern_map[color] = pattern
            used_patterns.add(pattern)
        else:
            if pattern_map[color] != pattern:
                return False
    
    return True

# Test cases




def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)