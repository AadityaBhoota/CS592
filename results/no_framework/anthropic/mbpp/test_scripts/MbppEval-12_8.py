def sort_matrix(M):
    """
    Write a function to sort a given matrix in ascending order according to the sum of its rows.

    Examples:
    sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]) == [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    sort_matrix([[5,8,9],[6,4,3],[2,1,4]]) == [[2, 1, 4], [6, 4, 3], [5, 8, 9]]
    """
    return sorted(M, key=lambda row: sum(row))

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)