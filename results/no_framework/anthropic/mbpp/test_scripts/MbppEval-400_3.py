def extract_freq(test_list):
    """
    Write a function to extract the number of unique tuples in the given list.

    Examples:
    extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
    extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)]) == 4
    extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)]) == 4
    """
    # Convert the list to a set to remove duplicates
    unique_tuples = set(test_list)
    return len(unique_tuples)

def check(candidate):
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4

check(extract_freq)