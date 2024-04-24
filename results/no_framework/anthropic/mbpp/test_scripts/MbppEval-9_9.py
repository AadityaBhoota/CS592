def find_Rotations(s):
    """
    Find the minimum number of rotations (greater than 0) required to get the same string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The minimum number of rotations required.
    """
    n = len(s)
    
    # If the string is empty or has only one character, return 1
    if n <= 1:
        return 1
    
    # Concatenate the string with itself
    double_s = s + s
    
    # Find the smallest prefix that is equal to the entire string
    for i in range(1, n+1):
        if double_s[i:i+n] == s:
            return i
    
    # If no such prefix is found, return the length of the string
    return n

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)