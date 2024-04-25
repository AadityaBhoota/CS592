def magic_square_test(my_matrix):
    n = len(my_matrix)
    if len(my_matrix[0]) != n:
        return False

    target_sum = sum(my_matrix[0])

    for i in range(n):
        row_sum = sum(my_matrix[i])
        col_sum = sum(my_matrix[j][i] for j in range(n))

        if row_sum != target_sum or col_sum != target_sum:
            return False

        if i == 0:
            diag_sum1 = my_matrix[i][i]
            diag_sum2 = my_matrix[i][n-i-1]

    if diag_sum1 != target_sum or diag_sum2 != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)