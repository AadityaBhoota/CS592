def count_bidirectional(test_list):
    bidirectional_counts = {}
    
    for pair in test_list:
        pair = tuple(sorted(pair))  # Sort the pair to ensure consistent comparison
        
        if pair not in bidirectional_counts:
            bidirectional_counts[pair] = 1
        else:
            bidirectional_counts[pair] += 1
    
    bidirectional_pairs = sum(count for count in bidirectional_counts.values() if count >= 2)
    
    return str(bidirectional_pairs)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)