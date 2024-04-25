def count_bidirectional(test_list):
    pair_count = {}

    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in pair_count:
            pair_count[reverse_pair] += 1
        else:
            pair_count[pair] = 1
            pair_count[reverse_pair] = 1

    bidirectional_count = sum(1 for count in pair_count.values() if count > 1)
    return str(bidirectional_count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)