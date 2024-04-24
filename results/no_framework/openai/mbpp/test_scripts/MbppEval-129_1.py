def magic_square_test(my_matrix):
    n = len(my_matrix)
    magic_sum = sum(my_matrix[0])

    # Check rows sum
    for row in my_matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check columns sum
    for j in range(n):
        col_sum = sum(my_matrix[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    # Check diagonal sum
    diag_sum = sum(my_matrix[i][i] for i in range(n))
    if diag_sum != magic_sum:
        return False

    # Check reverse diagonal sum
    rev_diag_sum = sum(my_matrix[i][n - i - 1] for i in range(n))
    if rev_diag_sum != magic_sum:
        return False

    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)