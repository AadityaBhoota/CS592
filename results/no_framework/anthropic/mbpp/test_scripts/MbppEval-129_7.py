def magic_square_test(my_matrix):
    """
    Write a function to calculate whether the matrix is a magic square.

    Examples:
    magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]) == False
    """
    # Check if the matrix is a square matrix
    if not all(len(row) == len(my_matrix) for row in my_matrix):
        return False

    # Calculate the sum of the elements in the first row
    target_sum = sum(my_matrix[0])

    # Check if the sum of the elements in each row, column, and diagonal is equal to the target sum
    for i in range(len(my_matrix)):
        # Check rows
        if sum(my_matrix[i]) != target_sum:
            return False

        # Check columns
        if sum(my_matrix[j][i] for j in range(len(my_matrix))) != target_sum:
            return False

    # Check the main diagonal
    if sum(my_matrix[i][i] for i in range(len(my_matrix))) != target_sum:
        return False

    # Check the secondary diagonal
    if sum(my_matrix[i][len(my_matrix) - 1 - i] for i in range(len(my_matrix))) != target_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)