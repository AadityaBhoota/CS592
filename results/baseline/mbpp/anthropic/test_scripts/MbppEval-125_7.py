def find_length(string):
    """
    Find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
    """
    max_diff = 0
    curr_diff = 0
    for char in string:
        if char == '0':
            curr_diff += 1
        else:
            curr_diff -= 1
        max_diff = max(max_diff, abs(curr_diff))
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)