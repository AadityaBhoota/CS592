def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    color_to_pattern = {}
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]

        if color in color_to_pattern:
            if color_to_pattern[color] != pattern:
                return False
        else:
            color_to_pattern[color] = pattern

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)