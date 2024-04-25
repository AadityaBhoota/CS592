def magic_square_test(my_matrix):
    num_rows = len(my_matrix)
    num_cols = len(my_matrix[0]) if num_rows > 0 else 0
    if num_rows != num_cols:
        return False

    expected_sum = sum(my_matrix[0])

    for row in my_matrix:
        if len(row) != num_cols:
            return False

        row_sum = sum(row)
        if row_sum != expected_sum:
            return False

    for col_idx in range(num_cols):
        col_sum = sum(row[col_idx] for row in my_matrix)
        if col_sum != expected_sum:
            return False

    diagonal_sum = sum(my_matrix[i][i] for i in range(num_cols))
    if diagonal_sum != expected_sum:
        return False

    secondary_diagonal_sum = sum(my_matrix[i][num_cols - 1 - i] for i in range(num_cols))
    if secondary_diagonal_sum != expected_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)