def magic_square_test(my_matrix):
    """
    Write a function to calculate whether the matrix is a magic square.

    Examples:
    magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True
    magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]) == False
    """
    # Step 3: Calculate the expected sum for each row, column, and diagonal
    magic_sum = sum(my_matrix[0])

    # Step 4: Check if the sum of each row is equal to the magic_sum
    for row in my_matrix:
        if sum(row) != magic_sum:
            return False

    # Step 5: Check if the sum of each column is equal to the magic_sum
    for i in range(len(my_matrix[0])):
        column_sum = 0
        for row in my_matrix:
            column_sum += row[i]
        if column_sum != magic_sum:
            return False

    # Step 6: Check if the sum of the main diagonal is equal to the magic_sum
    main_diagonal_sum = 0
    for i in range(len(my_matrix)):
        main_diagonal_sum += my_matrix[i][i]
    if main_diagonal_sum != magic_sum:
        return False

    # Step 7: Check if the sum of the secondary diagonal is equal to the magic_sum
    secondary_diagonal_sum = 0
    for i in range(len(my_matrix)):
        secondary_diagonal_sum += my_matrix[i][len(my_matrix[0]) - 1 - i]
    if secondary_diagonal_sum != magic_sum:
        return False

    # Step 8: If all the checks pass, return True
    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)