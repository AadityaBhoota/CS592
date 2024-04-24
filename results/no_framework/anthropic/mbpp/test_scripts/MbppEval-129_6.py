def magic_square_test(my_matrix):
    """
    Determines whether the given matrix is a magic square.

    Args:
        my_matrix (list of lists): The matrix to be tested.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is a square
    if not all(len(row) == len(my_matrix) for row in my_matrix):
        return False

    # Calculate the expected sum
    expected_sum = sum(my_matrix[0])

    # Check each row
    for row in my_matrix:
        if sum(row) != expected_sum:
            return False

    # Check each column
    for i in range(len(my_matrix)):
        column_sum = sum(row[i] for row in my_matrix)
        if column_sum != expected_sum:
            return False

    # Check the two diagonals
    diagonal_sum1 = sum(my_matrix[i][i] for i in range(len(my_matrix)))
    diagonal_sum2 = sum(my_matrix[i][len(my_matrix) - i - 1] for i in range(len(my_matrix)))
    if diagonal_sum1 != expected_sum or diagonal_sum2 != expected_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)