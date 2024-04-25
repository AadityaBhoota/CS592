def magic_square_test(my_matrix):
    # Check if the input matrix is not empty
    if len(my_matrix) == 0:
        return False
    
    # Check if the matrix is square
    if len(my_matrix) != len(my_matrix[0]):
        return False

    # Calculate the sum of the first row
    magic_sum = sum(my_matrix[0])

    # Check the sum of each row
    for row in my_matrix:
        if sum(row) != magic_sum:
            return False

    # Transpose the matrix to calculate column sums
    transposed_matrix = list(zip(*my_matrix))

    # Check the sum of each column
    for col in transposed_matrix:
        if sum(col) != magic_sum:
            return False

    # Check the sum of the main diagonal
    main_diagonal_sum = sum(my_matrix[i][i] for i in range(len(my_matrix)))
    if main_diagonal_sum != magic_sum:
        return False

    # Check the sum of the secondary diagonal
    secondary_diagonal_sum = sum(my_matrix[i][len(my_matrix) - i - 1] for i in range(len(my_matrix)))
    if secondary_diagonal_sum != magic_sum:
        return False

    # If all conditions are met, it's a Magic Square
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)