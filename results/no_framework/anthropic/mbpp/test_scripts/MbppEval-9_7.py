def find_Rotations(s):
    """
    Finds the minimum number of rotations (greater than 0) required to get the same string.
    
    Args:
        s (str): The input string.
        
    Returns:
        int: The minimum number of rotations required.
    """
    if not s:
        return 0
    
    n = len(s)
    for i in range(1, n):
        if s[:i] == s[n-i:]:
            return i
    
    return n

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)