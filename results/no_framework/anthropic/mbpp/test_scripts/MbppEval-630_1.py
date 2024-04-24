def get_coordinates(ele):
    """
    Write a function to extract all the adjacent coordinates of the given coordinate tuple.

    Examples:
    get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    get_coordinates((4, 5)) == [[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]
    """
    x, y = ele
    return [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]

def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)