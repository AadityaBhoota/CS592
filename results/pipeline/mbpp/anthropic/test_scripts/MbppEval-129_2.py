def magic_square_test(my_matrix):
    sum_constant = sum(my_matrix[0])
    for row in my_matrix:
        if sum(row) != sum_constant:
            return False
    for i in range(len(my_matrix)):
        column_sum = 0
        for row in my_matrix:
            column_sum += row[i]
        if column_sum != sum_constant:
            return False
    main_diagonal_sum = 0
    for i in range(len(my_matrix)):
        main_diagonal_sum += my_matrix[i][i]
    if main_diagonal_sum != sum_constant:
        return False
    secondary_diagonal_sum = 0
    for i in range(len(my_matrix)):
        secondary_diagonal_sum += my_matrix[i][len(my_matrix) - i - 1]
    if secondary_diagonal_sum != sum_constant:
        return False
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)