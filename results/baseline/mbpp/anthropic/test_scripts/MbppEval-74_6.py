def is_samepatterns(colors, patterns):
    """
    Check whether the colors list follows the sequence given in the patterns list.

    Args:
        colors (list): List of colors.
        patterns (list): List of patterns.

    Returns:
        bool: True if the colors list follows the sequence given in the patterns list, False otherwise.
    """
    if len(colors) != len(patterns):
        return False

    pattern_dict = {}
    for i, pattern in enumerate(patterns):
        if pattern not in pattern_dict:
            pattern_dict[pattern] = colors[i]
        elif pattern_dict[pattern] != colors[i]:
            return False

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)