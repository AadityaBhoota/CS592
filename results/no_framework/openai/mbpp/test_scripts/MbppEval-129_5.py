def magic_square_test(my_matrix):
    n = len(my_matrix)
    target_sum = 0

    # Calculate the sum of the first row (target sum)
    for num in my_matrix[0]:
        target_sum += num

    # Check rows
    for row in my_matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for i in range(n):
        col_sum = sum(row[i] for row in my_matrix)
        if col_sum != target_sum:
            return False

    # Check diagonals
    diagonal_1 = sum(my_matrix[i][i] for i in range(n))
    diagonal_2 = sum(my_matrix[i][n - i - 1] for i in range(n))
    if diagonal_1 != target_sum or diagonal_2 != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)