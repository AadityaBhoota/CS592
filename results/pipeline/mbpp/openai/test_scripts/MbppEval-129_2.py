def magic_square_test(my_matrix):
    def is_square_matrix(matrix):
        num_rows = len(matrix)
        for row in matrix:
            if len(row) != num_rows:
                return False
        return True

    if not is_square_matrix(my_matrix):
        return False

    target_sum = sum(my_matrix[0])

    for row in my_matrix[1:]:
        if sum(row) != target_sum:
            return False

    for col in range(len(my_matrix)):
        col_sum = sum(row[col] for row in my_matrix)
        if col_sum != target_sum:
            return False

    diagonal_sum1 = sum(my_matrix[i][i] for i in range(len(my_matrix)))
    diagonal_sum2 = sum(my_matrix[i][len(my_matrix)-1-i] for i in range(len(my_matrix)))

    return diagonal_sum1 == target_sum and diagonal_sum2 == target_sum

# Test the function




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)