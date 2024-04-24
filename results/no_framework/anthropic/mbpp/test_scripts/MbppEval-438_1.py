def count_bidirectional(test_list):
    """
    Write a function to count bidirectional tuple pairs.

    Examples:
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '3'
    count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '2'
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == '4'
    """
    bidirectional_pairs = set()
    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in test_list:
            bidirectional_pairs.add(tuple(sorted(pair)))

    return str(len(bidirectional_pairs))

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)