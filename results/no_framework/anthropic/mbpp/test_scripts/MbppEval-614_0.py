def cumulative_sum(test_list):
    """
    Find the cumulative sum of all the values that are present in the given tuple list.

    Args:
        test_list (list): A list of tuples.

    Returns:
        int: The cumulative sum of all the values in the given list of tuples.
    """
    total_sum = 0
    for tup in test_list:
        total_sum += sum(tup)
    return total_sum

def check(candidate):
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44

check(cummulative_sum)