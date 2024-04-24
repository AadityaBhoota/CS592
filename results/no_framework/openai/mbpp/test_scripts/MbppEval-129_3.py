def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False

    # Check columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False

    # Check first diagonal
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    # Check second diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_sum:
        return False
    
    return True

# Test cases




def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)