def find_length(string):
    """
    Find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.

    Args:
        string (str): The binary string.

    Returns:
        int: The maximum difference between the number of 0s and number of 1s in any sub-string.
    """
    max_diff = 0
    current_diff = 0
    for char in string:
        if char == '0':
            current_diff += 1
        else:
            current_diff -= 1
        max_diff = max(max_diff, abs(current_diff))
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)