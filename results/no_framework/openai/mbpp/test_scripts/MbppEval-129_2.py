def magic_square_test(my_matrix):
    n = len(my_matrix)
    
    # Calculate sum of diagonal elements
    diag_sum1 = sum(my_matrix[i][i] for i in range(n))
    diag_sum2 = sum(my_matrix[i][n-i-1] for i in range(n))
    
    if diag_sum1 != diag_sum2:
        return False
    
    # Calculate sum of rows and columns
    for i in range(n):
        if sum(my_matrix[i]) != diag_sum1 or sum(row[i] for row in my_matrix) != diag_sum1:
            return False
    
    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)