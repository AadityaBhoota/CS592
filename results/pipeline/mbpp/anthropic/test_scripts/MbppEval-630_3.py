def adjac(ele, sub = []):
    x_coords = []
    y_coords = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            new_x = ele[0] + dx
            new_y = ele[1] + dy
            if new_x >= 0 and new_y >= 0:
                sub.append((new_x, new_y))
    return sub

def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)