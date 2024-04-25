def sort_matrix(M):
    row_sums = [sum(row) for row in M]
    rows_with_sums = list(enumerate(row_sums))
    rows_with_sums.sort(key=lambda x: x[1])
    
    sorted_matrix = [M[row[0]] for row in rows_with_sums]
    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)