def find_first_occurrence(A, x):
    '''
    Write a function to find the index of the first occurrence of a given number in a sorted array.

    Examples:
    find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4
    '''
            # Step 3: Return Index
            return mid

def check(candidate):
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4

check(find_first_occurrence)