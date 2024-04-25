def magic_square_test(my_matrix):
    """
    Write a function to calculate whether the matrix is a magic square.

    Examples:
    magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]) == False
    """
    # Check if the matrix is square
    if not all(len(row) == len(my_matrix) for row in my_matrix):
        return False

    # Calculate the expected sum
    expected_sum = sum(my_matrix[0])

    # Check if the rows, columns, and diagonals all have the expected sum
    for row in my_matrix:
        if sum(row) != expected_sum:
            return False
    for i in range(len(my_matrix)):
        if sum(row[i] for row in my_matrix) != expected_sum:
            return False
    if sum(my_matrix[i][i] for i in range(len(my_matrix))) != expected_sum:
        return False
    if sum(my_matrix[i][len(my_matrix) - i - 1] for i in range(len(my_matrix))) != expected_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)