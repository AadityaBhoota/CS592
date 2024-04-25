def count_bidirectional(test_list):
    tuple_dict = {}
    count = 0
    for t in test_list:
        reverse_t = (t[1], t[0])
        if reverse_t in tuple_dict:
            count += 1
            tuple_dict.pop(reverse_t)
        else:
            tuple_dict[t] = reverse_t
    return str(count)

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 2
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == 4

check(count_bidirectional)