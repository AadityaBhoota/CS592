def adjac(coord, sub=[]):
    adj_coords = []
    for i in range(coord[0] - 1, coord[0] + 2):
        for j in range(coord[1] - 1, coord[1] + 2):
            if (i, j) != coord:
                adj_coords.append([i, j])
    return adj_coords

# Testing the function



def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)