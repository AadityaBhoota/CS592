def count_bidirectional(test_list):
    count = 0
    pair_set = set()
    for pair in test_list:
        reversed_pair = (pair[1], pair[0])
        if pair in pair_set or reversed_pair in pair_set:
            count += 1
            pair_set.discard(pair)
            pair_set.discard(reversed_pair)
        else:
            pair_set.add(pair)
    return str(count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)