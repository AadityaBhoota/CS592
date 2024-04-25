def find_first_occurrence(A, x):
    index = -1  # Initializing index to -1
    
    for i, num in enumerate(A):
        if num == x and index == -1:
            index = i  # Updating the index to the current index
    
    return index

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

check(find_first_occurrence)