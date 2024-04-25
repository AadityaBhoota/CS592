def magic_square_test(my_matrix):
    """
    Calculates whether the given matrix is a magic square.

    A magic square is a square matrix where the sum of each row, column, and
    the two main diagonals are all equal.

    Args:
        my_matrix (list of lists): A square matrix represented as a list of lists.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is square
    n = len(my_matrix)
    if len(my_matrix[0]) != n:
        return False

    # Calculate the target sum
    target_sum = sum(my_matrix[0])

    # Check rows
    for row in my_matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for i in range(n):
        if sum([row[i] for row in my_matrix]) != target_sum:
            return False

    # Check main diagonal
    if sum([my_matrix[i][i] for i in range(n)]) != target_sum:
        return False

    # Check secondary diagonal
    if sum([my_matrix[i][n - 1 - i] for i in range(n)]) != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)