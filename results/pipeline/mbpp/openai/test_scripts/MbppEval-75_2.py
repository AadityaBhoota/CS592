def find_tuples(test_list, K):
    result_tuples = []
    if not test_list:
        return '[]'
    
    for tpl in test_list:
        if all(elem % K == 0 for elem in tpl):
            result_tuples.append(tpl)
    
    return str(result_tuples)

def check(candidate):
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
    assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)]

check(find_tuples)