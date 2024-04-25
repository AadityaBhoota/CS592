def find_Rotations(s):
    """
    Find the minimum number of rotations (greater than 0) required to get the same string.

    Args:
        s (str): The input string.

    Returns:
        int: The minimum number of rotations required.
    """
    n = len(s)
    if n == 0:
        return 0

    # Concatenate the string with itself
    doubled_s = s + s

    # Find the smallest substring that matches the original string
    for i in range(1, n + 1):
        if doubled_s[i:i + n] == s:
            return i

    # If no match is found, the string cannot be rotated to the same string
    return n

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)