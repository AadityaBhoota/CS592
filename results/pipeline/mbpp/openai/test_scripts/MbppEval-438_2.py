def count_bidirectional(test_list):
    bidirectional_pairs = {}
    
    for pair in test_list:
        sorted_pair = tuple(sorted(pair))
        tuple_list = list(sorted_pair)
        
        if tuple_list in bidirectional_pairs:
            bidirectional_pairs[tuple_list] += 1
        else:
            bidirectional_pairs[tuple_list] = 1
    
    count = 0
    for pair_count in bidirectional_pairs.values():
        if pair_count == 2:
            count += 1
    
    return str(count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)