def sort_matrix(M):
    row_sums = [sum(row) for row in M]
    rows_dict = dict(zip(row_sums, M))
    
    sorted_rows = dict(sorted(rows_dict.items(), key=lambda x: x[0]))
    
    sorted_matrix = list(sorted_rows.values())
    return sorted_matrix

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)