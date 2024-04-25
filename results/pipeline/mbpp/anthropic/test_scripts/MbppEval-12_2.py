def sort_matrix(M):
    row_sums = [sum(row) for row in M]
    row_tuples = [(row_sum, row) for row_sum, row in zip(row_sums, M)]
    sorted_row_tuples = sorted(row_tuples)
    sorted_matrix = [row for _, row in sorted_row_tuples]
    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)