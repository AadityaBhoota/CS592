def find_Rotations(s):
    """
    Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.

    Examples:
    find_Rotations("aaaa") == 1
    find_Rotations("ab") == 2
    find_Rotations("abc") == 3
    """
    if not s:
        return 0

    length = len(s)
    for i in range(1, length):
        if s[:i] == s[length-i:]:
            return i

    return length

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3

check(find_Rotations)