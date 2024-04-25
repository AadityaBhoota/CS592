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
    
    # Create a dictionary to map colors to patterns
    color_to_pattern = {}
    
    for i in range(len(colors)):
        color = colors[i]
        pattern = patterns[i]
        
        # If the color is not in the dictionary, add it
        if color not in color_to_pattern:
            color_to_pattern[color] = pattern
        # If the color is in the dictionary, check if the pattern matches
        elif color_to_pattern[color] != pattern:
            return False
    
    return True

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False

check(is_samepatterns)