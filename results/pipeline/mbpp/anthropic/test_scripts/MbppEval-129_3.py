def magic_square_test(my_matrix):
    # Check if the input is a valid 2D matrix
    if not isinstance(my_matrix, list) or not all(isinstance(row, list) for row in my_matrix):
        return False
    
    # Check if all rows have the same length
    row_length = len(my_matrix[0])
    if not all(len(row) == row_length for row in my_matrix):
        return False
    
    # Initialize magic_sum
    magic_sum = sum(my_matrix[0])
    
    # Check rows
    for row in my_matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check columns
    for j in range(row_length):
        column_sum = 0
        for i in range(len(my_matrix)):
            column_sum += my_matrix[i][j]
        if column_sum != magic_sum:
            return False
    
    # Calculate primary diagonal sum
    primary_diagonal_sum = 0
    for i in range(len(my_matrix)):
        primary_diagonal_sum += my_matrix[i][i]
    
    # Calculate secondary diagonal sum
    secondary_diagonal_sum = 0
    for i in range(len(my_matrix)):
        secondary_diagonal_sum += my_matrix[i][row_length - i - 1]
    
    # Check diagonals
    if primary_diagonal_sum != magic_sum or secondary_diagonal_sum != magic_sum:
        return False
    
    # If all checks pass, return True
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)