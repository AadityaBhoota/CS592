def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    color_map = {}
    for i, pattern in enumerate(patterns):
        if pattern not in color_map:
            color_map[pattern] = colors[i]
        elif color_map[pattern] != colors[i]:
            return False

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)