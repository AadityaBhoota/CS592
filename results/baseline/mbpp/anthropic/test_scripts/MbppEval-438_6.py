def count_bidirectional(test_list):
    """
    Write a function to count bidirectional tuple pairs.

    Examples:
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == '3'
    count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)]) == '2'
    count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)]) == '4'
    """
    # Create a set to store unique pairs
    unique_pairs = set()

    # Count the number of bidirectional pairs
    for pair in test_list:
        reversed_pair = (pair[1], pair[0])
        if reversed_pair in unique_pairs:
            unique_pairs.remove(reversed_pair)
        else:
            unique_pairs.add(pair)

    return str(len(unique_pairs))

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)