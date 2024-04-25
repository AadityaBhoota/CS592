def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    
    map_colors = {}
    map_patterns = {}
    
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]
        
        if color not in map_colors:
            map_colors[color] = pattern
        else:
            if map_colors[color] != pattern:
                return False
        
        if pattern not in map_patterns:
            map_patterns[pattern] = color
        else:
            if map_patterns[pattern] != color:
                return False
    
    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)