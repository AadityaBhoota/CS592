def find_length(string):
    """
    Find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
    
    Args:
        string (str): The binary string to search.
    
    Returns:
        int: The maximum difference between 0s and 1s.
    """
    max_diff = 0
    count_0 = 0
    count_1 = 0
    
    for char in string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        
        diff = abs(count_0 - count_1)
        max_diff = max(max_diff, diff)
    
    return max_diff

def check(candidate):
    assert find_length("11000010001") == 6
    assert find_length("10111") == 1
    assert find_length("11011101100101") == 2

check(find_length)