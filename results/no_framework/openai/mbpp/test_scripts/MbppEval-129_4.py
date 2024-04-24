def magic_square_test(my_matrix):
    n = len(my_matrix)
    
    # Calculate the sum of the first row
    target_sum = sum(my_matrix[0])
    
    # Check the sum of rows
    for row in my_matrix:
        if sum(row) != target_sum:
            return False
    
    # Check the sum of columns
    for j in range(n):
        col_sum = sum(my_matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False
    
    # Check the sum of the main diagonal
    if sum(my_matrix[i][i] for i in range(n)) != target_sum:
        return False
    
    # Check the sum of the secondary diagonal
    if sum(my_matrix[i][n-1-i] for i in range(n)) != target_sum:
        return False
    
    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)