def magic_square_test(my_matrix):
    # Check if the matrix is a square matrix
    n = len(my_matrix)
    if not all(len(row) == n for row in my_matrix):
        return False

    # Calculate the sum of the first row
    target_sum = sum(my_matrix[0])

    # Check rows
    if any(sum(row) != target_sum for row in my_matrix):
        return False

    # Check columns
    if any(sum(col) != target_sum for col in zip(*my_matrix)):
        return False

    # Check diagonals
    diagonal1 = [my_matrix[i][i] for i in range(n)]
    diagonal2 = [my_matrix[i][n - 1 - i] for i in range(n)]
    if sum(diagonal1) != target_sum or sum(diagonal2) != target_sum:
        return False

    return True

# Test Cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)