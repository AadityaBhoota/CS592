def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    color_to_pattern = {}
    pattern_to_color = {}

    for i in range(len(colors)):
        color, pattern = colors[i], patterns[i]

        if pattern not in pattern_to_color:
            if color in color_to_pattern:
                return False
            color_to_pattern[color] = pattern
            pattern_to_color[pattern] = color
        elif pattern_to_color[pattern] != color:
            return False

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)