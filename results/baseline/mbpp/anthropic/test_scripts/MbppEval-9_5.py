def find_Rotations(string):
    """
    Find the minimum number of rotations (greater than 0) required to get the same string.

    Args:
        string (str): The input string.

    Returns:
        int: The minimum number of rotations required.
    """
    if not string:
        return 0

    n = len(string)
    for i in range(1, n):
        if string[:i] == string[n-i:]:
            return i

    return n

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)