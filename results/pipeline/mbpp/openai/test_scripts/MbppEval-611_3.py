def max_of_nth(test_list, N):
    max_val = float('-inf')
    for sublist in test_list:
        if sublist[N] > max_val:
            max_val = sublist[N]
    return max_val

def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)