def sort_matrix(M):
    row_sums = []
    for row in M:
        row_sum = sum(row)
        row_sums.append(row_sum)
    sorted_matrix = []
    for row_sum in sorted(row_sums):
        index = row_sums.index(row_sum)
        sorted_matrix.append(M[index])
    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)