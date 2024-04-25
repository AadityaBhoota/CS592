def count_bidirectional(test_list):
    bidirectional_pairs = set()
    for tup in test_list:
        reverse_tup = (tup[1], tup[0])
        if reverse_tup in test_list:
            bidirectional_pairs.add(tuple(sorted(tup)))
    return str(len(bidirectional_pairs))

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)