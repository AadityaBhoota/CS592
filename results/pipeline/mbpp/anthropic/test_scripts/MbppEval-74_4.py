def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    color_to_pattern = {}

    for i in range(len(colors)):
        color, pattern = colors[i], patterns[i]
        if color not in color_to_pattern:
            if pattern in color_to_pattern.values():
                return False
            color_to_pattern[color] = pattern
        elif color_to_pattern[color] != pattern:
            return False

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)