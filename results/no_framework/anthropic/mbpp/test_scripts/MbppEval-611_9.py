def max_of_nth(test_list, N):
    """
    Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
    
    Examples:
    max_of_nth([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 19
    max_of_nth([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 10
    max_of_nth([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 1) == 11
    """
    max_values = []
    for i in range(len(test_list[0])):
        column_values = [row[i] for row in test_list]
        max_values.append(max(column_values))
    return max_values[N-1]

def check(candidate):
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

check(max_of_nth)