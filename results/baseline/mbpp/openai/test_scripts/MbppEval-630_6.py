def adjac(ele, sub = []): 
    '''
    Write a function to extract all the adjacent coordinates of the given coordinate tuple.

    Examples:
    get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    get_coordinates((4, 5)) == [[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]
    '''
def get_coordinates(coord):
    adj_coords = []
    for i in range(coord[0]-1, coord[0]+2):
        for j in range(coord[1]-1, coord[1]+2):
            adj_coords.append([i, j])
    return adj_coords

# Test the function with the provided examples




def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)