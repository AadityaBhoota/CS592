def sort_matrix(M):
    row_sums = []
    for row in M:
        row_sums.append(sum(row))

    sorted_indices = sorted(range(len(M)), key=lambda x: row_sums[x])
    sorted_matrix = [M[i] for i in sorted_indices]

    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)