def magic_square_test(my_matrix):
    n = len(my_matrix)
    
    # Calculate the sum for the first row to use as a reference
    reference_sum = sum(my_matrix[0])
    
    # Check if sum of each row is equal to the reference sum
    for row in my_matrix:
        if sum(row) != reference_sum:
            return False
    
    # Check if sum of each column is equal to the reference sum
    for i in range(n):
        col_sum = sum(row[i] for row in my_matrix)
        if col_sum != reference_sum:
            return False

    # Check if sum of the main diagonal is equal to the reference sum
    if sum(my_matrix[i][i] for i in range(n)) != reference_sum:
        return False
    
    # Check if sum of the secondary diagonal is equal to the reference sum
    if sum(my_matrix[i][n - i - 1] for i in range(n)) != reference_sum:
        return False
    
    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)