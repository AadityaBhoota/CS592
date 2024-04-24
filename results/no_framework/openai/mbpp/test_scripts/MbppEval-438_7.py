def count_bidirectional(test_list):
    count = 0
    set_pairs = set()
    
    for pair in test_list:
        reverse_pair = tuple(reversed(pair))
        if pair in set_pairs or reverse_pair in set_pairs:
            count += 1
        else:
            set_pairs.add(pair)
    
    return str(count)

# Test cases




def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)