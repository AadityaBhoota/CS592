def max_difference(test_list):
    """
    Write a function to find the maximum difference between available pairs in the given tuple list.

    Examples:
    max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
    """
    max_diff = 0
    for a, b in test_list:
        diff = abs(b - a)
        max_diff = max(max_diff, diff)
    return max_diff

def check(candidate):
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23

check(max_difference)