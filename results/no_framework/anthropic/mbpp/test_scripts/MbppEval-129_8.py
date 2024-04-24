def magic_square_test(my_matrix):
    """
    Check if the given matrix is a magic square.

    A magic square is a square matrix of numbers where the sum of each row, column, and
    both diagonals is the same.

    Args:
        my_matrix (list of lists): The matrix to be tested.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is square
    if not all(len(row) == len(my_matrix) for row in my_matrix):
        return False

    # Calculate the target sum
    target_sum = sum(my_matrix[0])

    # Check if the sums of the rows, columns, and diagonals are equal to the target sum
    for i in range(len(my_matrix)):
        # Check row sum
        if sum(my_matrix[i]) != target_sum:
            return False

        # Check column sum
        if sum(row[i] for row in my_matrix) != target_sum:
            return False

    # Check main diagonal sum
    if sum(my_matrix[i][i] for i in range(len(my_matrix))) != target_sum:
        return False

    # Check secondary diagonal sum
    if sum(my_matrix[i][len(my_matrix) - 1 - i] for i in range(len(my_matrix))) != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)