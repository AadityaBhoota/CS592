def max_of_nth(test_list, N):
    if not test_list or any(len(row) < N for row in test_list):
        raise ValueError("Invalid input list. Each row must have at least N elements.")

    max_value = test_list[0][N-1]

    for row in test_list:
        max_value = max(max_value, row[N-1])

    return max_value

def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)