def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    color_to_pattern = {}
    pattern_to_color = {}

    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]

        if color in color_to_pattern:
            if color_to_pattern[color] != pattern:
                return False
        else:
            color_to_pattern[color] = pattern

        if pattern in pattern_to_color:
            if pattern_to_color[pattern] != color:
                return False
        else:
            pattern_to_color[pattern] = color

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)