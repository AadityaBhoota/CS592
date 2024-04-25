def extract_freq(test_list):
    freq_dict = {}
    for tup in test_list:
        if tup not in freq_dict:
            freq_dict[tup] = 1
        else:
            freq_dict[tup] += 1
    return len(freq_dict)

def check(candidate):
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4

check(extract_freq)