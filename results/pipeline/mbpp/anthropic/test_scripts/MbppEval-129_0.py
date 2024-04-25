def magic_square_test(my_matrix):
    """
    Determine if the input matrix is a magic square.
    
    Args:
        my_matrix (list of lists): A square matrix.
    
    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    n = len(my_matrix)
    for row in my_matrix:
        if len(row) != n:
            return False
    
    expected_sum = sum(my_matrix[0])
    
    for row in my_matrix:
        if sum(row) != expected_sum:
            return False
    
    for i in range(n):
        column_sum = 0
        for j in range(n):
            column_sum += my_matrix[j][i]
        if column_sum != expected_sum:
            return False
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += my_matrix[i][i]
    if diagonal_sum != expected_sum:
        return False
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += my_matrix[i][n-1-i]
    if diagonal_sum != expected_sum:
        return False
    
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)