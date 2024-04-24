def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False

    mapping = {}
    for i in range(len(colors)):
        if colors[i] not in mapping:
            mapping[colors[i]] = patterns[i]
        elif mapping[colors[i]] != patterns[i]:
            return False

    return True

# Test cases




def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)