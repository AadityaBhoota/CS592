def extract_freq(test_list):
    unique_tuples = set(test_list)
    return len(unique_tuples)

# Test cases




def check(candidate):
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4

check(extract_freq)