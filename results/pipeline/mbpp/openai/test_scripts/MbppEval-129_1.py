def magic_square_test(my_matrix):
    reference_sum = sum(my_matrix[0])

    # Check rows
    for row in my_matrix:
        if sum(row) != reference_sum:
            return False

    # Check columns
    for i in range(len(my_matrix)):
        col_sum = sum(row[i] for row in my_matrix)
        if col_sum != reference_sum:
            return False

    # Check main diagonal
    if sum(my_matrix[i][i] for i in range(len(my_matrix))) != reference_sum:
        return False

    # Check secondary diagonal
    if sum(my_matrix[i][len(my_matrix)-1-i] for i in range(len(my_matrix))) != reference_sum:
        return False

    return True

def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)