def Extract(lst):
    first_elements = []
    
    for sublist in lst:
        if sublist:  # Check if sublist is not empty
            first_elements.append(sublist[0])
        
    return first_elements

def check(candidate):
    assert Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert Extract([[1,2,3],[4, 5]]) == [1,4]
    assert Extract([[9,8,1],[1,2]]) == [9,1]

check(Extract)