To determine whether a given matrix is a magic square, we need to check the following conditions:
1. The sum of each row must be equal.
2. The sum of each column must be equal.
3. The sum of each of the two diagonals must be equal.

Let's implement the `magic_square_test` function:
def check(candidate):
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

check(magic_square_test)