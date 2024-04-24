def magic_square_test(my_matrix):
    """
    Checks if the given matrix is a magic square.

    Args:
        my_matrix (list): A 2D list representing the matrix.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Get the size of the matrix
    n = len(my_matrix)

    # Check if the matrix is square
    if any(len(row) != n for row in my_matrix):
        return False

    # Calculate the expected sum for each row, column, and diagonal
    expected_sum = sum(my_matrix[0])

    # Check if the sum of each row is equal to the expected sum
    if any(sum(row) != expected_sum for row in my_matrix):
        return False

    # Check if the sum of each column is equal to the expected sum
    if any(sum(col) != expected_sum for col in zip(*my_matrix)):
        return False

    # Check if the sum of the main diagonal is equal to the expected sum
    if sum(my_matrix[i][i] for i in range(n)) != expected_sum:
        return False

    # Check if the sum of the secondary diagonal is equal to the expected sum
    if sum(my_matrix[i][n-1-i] for i in range(n)) != expected_sum:
        return False

    # If all checks pass, the matrix is a magic square
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)