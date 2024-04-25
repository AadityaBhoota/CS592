def adjac(ele, sub=[]):
    x, y = ele  # Step 1: Get the x and y coordinates from the given element tuple
    adjacent_coords = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2)]  # Step 2: Generate adjacent coordinates around the given coordinate
    adjacent_coords.remove(ele)  # Step 3: Exclude the current element from the adjacent coordinates
    adjacent_coords = [list(coord) for coord in adjacent_coords]  # Step 4: Convert adjacent coordinates to list of lists
    return adjacent_coords

def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)