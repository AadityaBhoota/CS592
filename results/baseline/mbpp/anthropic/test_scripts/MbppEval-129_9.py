def magic_square_test(my_matrix):
    """
    Determines whether a given square matrix is a magic square.

    A magic square is a square matrix of numbers where the sum of each row, column, and
    the two main diagonals is the same.

    Args:
        my_matrix (list of lists): A square matrix represented as a list of lists.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is square (same number of rows and columns)
    if len(my_matrix) != len(my_matrix[0]):
        return False

    # Calculate the expected sum for each row, column, and diagonal
    expected_sum = sum(my_matrix[0])

    # Check the sums of rows
    for row in my_matrix:
        if sum(row) != expected_sum:
            return False

    # Check the sums of columns
    for j in range(len(my_matrix)):
        column_sum = 0
        for i in range(len(my_matrix)):
            column_sum += my_matrix[i][j]
        if column_sum != expected_sum:
            return False

    # Check the sum of the main diagonal
    diagonal_sum = 0
    for i in range(len(my_matrix)):
        diagonal_sum += my_matrix[i][i]
    if diagonal_sum != expected_sum:
        return False

    # Check the sum of the secondary diagonal
    diagonal_sum = 0
    for i in range(len(my_matrix)):
        diagonal_sum += my_matrix[i][len(my_matrix) - 1 - i]
    if diagonal_sum != expected_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)