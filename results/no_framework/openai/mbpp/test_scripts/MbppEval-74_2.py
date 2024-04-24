def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    pattern_map = {}
    color_map = {}

    for color, pattern in zip(colors, patterns):
        if color not in color_map and pattern not in pattern_map:
            color_map[color] = pattern
            pattern_map[pattern] = color
        elif color in color_map and pattern in pattern_map:
            if color_map[color] != pattern or pattern_map[pattern] != color:
                return False
        else:
            return False

    return True

# Test cases




def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)