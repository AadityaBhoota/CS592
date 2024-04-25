def max_difference(test_list):
    """
    Find the maximum difference between available pairs in the given tuple list.
    
    Args:
        test_list (list): A list of tuples, where each tuple contains two integers.
    
    Returns:
        int: The maximum difference between the pairs in the list.
    """
    max_diff = 0
    for a, b in test_list:
        diff = abs(a - b)
        max_diff = max(max_diff, diff)
    return max_diff

def check(candidate):
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

check(max_difference)