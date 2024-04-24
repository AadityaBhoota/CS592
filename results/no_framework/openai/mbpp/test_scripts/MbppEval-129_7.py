def magic_square_test(my_matrix):
    n = len(my_matrix)
    
    # Sum of elements in the first row
    sum_first_row = sum(my_matrix[0])
    
    # Check rows
    for row in my_matrix:
        if sum(row) != sum_first_row:
            return False
    
    # Check columns
    for j in range(n):
        column_sum = sum(row[j] for row in my_matrix)
        if column_sum != sum_first_row:
            return False
    
    # Check diagonal (top-left to bottom-right)
    diagonal_sum = sum(my_matrix[i][i] for i in range(n))
    if diagonal_sum != sum_first_row:
        return False
    
    # Check diagonal (top-right to bottom-left)
    reverse_diagonal_sum = sum(my_matrix[i][n - i - 1] for i in range(n))
    if reverse_diagonal_sum != sum_first_row:
        return False
    
    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)