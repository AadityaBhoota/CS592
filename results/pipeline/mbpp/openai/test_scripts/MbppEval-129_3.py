def magic_square_test(my_matrix):
    n = len(my_matrix)
    if n == 0:
        return False  # Empty matrix is not a magic square
        
    # Calculate sum of the first row
    sum_row = sum(my_matrix[0])
    
    # Check sum of the rows
    for i in range(1, n):
        if sum(my_matrix[i]) != sum_row:
            return False  # Rows don't have the same sum
            
    # Check sum of the columns
    for i in range(n):
        col_sum = sum(row[i] for row in my_matrix)
        if col_sum != sum_row:
            return False  # Columns don't have the same sum
    
    # Check sum of the diagonals
    diag_sum1 = sum(my_matrix[i][i] for i in range(n))
    diag_sum2 = sum(my_matrix[i][n-1-i] for i in range(n))
    if diag_sum1 != sum_row or diag_sum2 != sum_row:
        return False  # Diagonals don't have the same sum
        
    # Check if all sums are equal
    if sum_row != diag_sum1 or sum_row != diag_sum2:
        return False  # Sums are not equal
        
    return True  # Matrix is a magic square

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)