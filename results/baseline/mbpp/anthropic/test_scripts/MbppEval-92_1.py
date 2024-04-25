def is_undulating(n):
    """
    Check whether the given number is undulating or not.

    Examples:
    is_undulating("1212121") == True
    is_undulating("1991") == False
    is_undulating("121") == True
    """
    n = str(n)  # Convert the input to a string
    
    if len(n) < 2:
        return False  # A number with less than 2 digits is not undulating
    
    # Check if the digits alternate between increasing and decreasing
    is_increasing = None
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            return False  # Digits should not be equal
        
        if is_increasing is None:
            is_increasing = int(n[i]) > int(n[i-1])
        elif is_increasing != (int(n[i]) > int(n[i-1])):
            is_increasing = not is_increasing
        else:
            return False  # Digits should alternate between increasing and decreasing
    
    return True

def check(candidate):
    assert is_undulating(1212121) == True
    assert is_undulating(1991) == False
    assert is_undulating(121) == True

check(is_undulating)