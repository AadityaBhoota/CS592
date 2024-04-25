def magic_square_test(my_matrix):
    """
    Checks whether the given matrix is a magic square.

    Args:
        my_matrix (list of lists): The matrix to be tested.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is square
    n = len(my_matrix)
    if any(len(row) != n for row in my_matrix):
        return False

    # Check if the sum of each row is the same
    target_sum = sum(my_matrix[0])
    if any(sum(row) != target_sum for row in my_matrix):
        return False

    # Check if the sum of each column is the same
    if any(sum(col) != target_sum for col in zip(*my_matrix)):
        return False

    # Check if the sum of the diagonals is the same
    diagonal_sum1 = sum(my_matrix[i][i] for i in range(n))
    diagonal_sum2 = sum(my_matrix[i][n-i-1] for i in range(n))
    if diagonal_sum1 != diagonal_sum2 or diagonal_sum1 != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)