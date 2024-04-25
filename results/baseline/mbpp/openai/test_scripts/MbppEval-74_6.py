def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    mapping = {}
    pattern_set = set()
    
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]
        
        if color in mapping:
            if mapping[color] != pattern:
                return False
        else:
            mapping[color] = pattern
        
        pattern_set.add(pattern)
    
    return len(set(mapping.values())) == len(pattern_set)

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)