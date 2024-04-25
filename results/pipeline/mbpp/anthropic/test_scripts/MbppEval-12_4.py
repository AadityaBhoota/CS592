def sort_matrix(M):
    row_sums = []
    for row in M:
        row_sum = sum(row)
        row_sums.append(row_sum)
    zipped_rows = list(zip(M, row_sums))
    zipped_rows.sort(key=lambda x: x[1])
    sorted_rows = [row[0] for row in zipped_rows]
    return sorted_rows

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)