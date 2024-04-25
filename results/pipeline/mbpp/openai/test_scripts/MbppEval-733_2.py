def find_first_occurrence(A, x):
    first_index = -1
    
    for index, element in enumerate(A):
        if element == x:
            first_index = index
            break
 
        elif element > x:
            break

    return first_index

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

check(find_first_occurrence)