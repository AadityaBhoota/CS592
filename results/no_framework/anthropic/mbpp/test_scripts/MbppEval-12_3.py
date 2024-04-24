def sort_matrix(M):
    """
    Sorts a given matrix in ascending order according to the sum of its rows.
    
    Args:
    M (list): A 2D list representing the matrix.
    
    Returns:
    list: The sorted matrix.
    """
    # Sort the matrix based on the sum of each row
    M.sort(key=lambda row: sum(row))
    
    return M

def check(candidate):
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]])==[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5,8,9],[6,4,3],[2,1,4]])==[[2, 1, 4], [6, 4, 3], [5, 8, 9]]

check(sort_matrix)