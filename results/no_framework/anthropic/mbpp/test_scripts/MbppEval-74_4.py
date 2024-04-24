def is_samepatterns(colors, patterns):
    """
    Write a function to check whether it follows the sequence given in the patterns array.

    Examples:
    is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
    is_samepatterns(["red","green","greenn"], ["a","b","b"]) == False
    is_samepatterns(["red","green","greenn"], ["a","b"]) == False
    """
    if len(colors) != len(patterns):
        return False

    color_to_pattern = {}
    for i in range(len(colors)):
        if colors[i] in color_to_pattern:
            if color_to_pattern[colors[i]] != patterns[i]:
                return False
        else:
            color_to_pattern[colors[i]] = patterns[i]

    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)