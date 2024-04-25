def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False

    pattern_to_color = {}

    for i in range(len(colors)):
        pattern = patterns[i]
        color = colors[i]

        if pattern not in pattern_to_color:
            if color in pattern_to_color.values():
                return False
            pattern_to_color[pattern] = color
        elif pattern_to_color[pattern] != color:
            return False

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)