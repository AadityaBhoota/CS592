def sort_matrix(M):
    row_sums = []
    row_to_sum = {}
    for row in M:
        row_sum = sum(row)
        row_sums.append(row_sum)
        row_to_sum[row_sum] = row

    sorted_keys = sorted(row_to_sum.keys())
    sorted_matrix = [row_to_sum[key] for key in sorted_keys]

    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)