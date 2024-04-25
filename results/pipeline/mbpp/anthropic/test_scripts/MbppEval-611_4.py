def max_of_nth(test_list, N):
    if not isinstance(test_list, list) or not all(isinstance(inner_list, tuple) for inner_list in test_list):
        raise ValueError("test_list must be a list of tuples")
    if N < 0 or N >= len(test_list[0]):
        raise ValueError("N must be a valid index within the range of the inner lists")

    max_value = float('-inf')
    for inner_list in test_list:
        max_value = max(max_value, inner_list[N])

    return max_value

def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)