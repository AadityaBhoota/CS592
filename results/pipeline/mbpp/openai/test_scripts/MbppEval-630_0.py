def adjac(ele, sub=[]): 
    x, y = ele
    coordinates = []
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) != (x, y):
                coordinates.append([i, j])
    
    return coordinates

# Testing the function


def check(candidate):
    assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    assert get_coordinates((4, 5)) ==[[3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 4], [5, 5], [5, 6]]
    assert get_coordinates((5, 6)) == [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7]]

check(adjac)