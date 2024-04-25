def count_bidirectional(test_list):
    count = 0
    bidirectional_pairs = set()
    
    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if reverse_pair in bidirectional_pairs:
            count += 1
            bidirectional_pairs.remove(reverse_pair)
        else:
            bidirectional_pairs.add(pair)
    
    return str(count)

# Test cases




def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)