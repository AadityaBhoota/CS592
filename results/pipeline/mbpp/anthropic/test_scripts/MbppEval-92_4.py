def is_undulating(n):
    """
    Check whether the given number is undulating or not.

    Examples:
    is_undulating("1212121") == True
    is_undulating("1991") == False
    is_undulating("121") == True
    is_undulating(1212121) == True
    is_undulating(1991) == False
    is_undulating(121) == True
    is_undulating("") == False
    is_undulating(1) == False
    """
    # Convert the input to a string if it's a number
    n_str = str(n)
    
    # Check for edge cases
    if len(n_str) < 2:
        return False
    
    # Iterate through the digits, checking the alternating pattern
    is_undulating = True
    for i in range(len(n_str) - 2):
        if (int(n_str[i]) - int(n_str[i+1])) * (int(n_str[i+1]) - int(n_str[i+2])) >= 0:
            is_undulating = False
            break
    
    return is_undulating

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)