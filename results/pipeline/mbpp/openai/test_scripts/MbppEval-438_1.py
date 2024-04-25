def count_bidirectional(test_list):
    count = 0
    checked_pairs = set()
    
    for tup in test_list:
        reverse_tup = (tup[1], tup[0])
        
        if tup not in checked_pairs and reverse_tup in test_list:
            count += 1
            checked_pairs.add(tup)
    
    return str(count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)