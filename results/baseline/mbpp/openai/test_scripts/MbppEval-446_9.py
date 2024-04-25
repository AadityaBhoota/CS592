def count_Occurrence(tup, lst):
    '''
    Function to count the occurence of all elements of list in a tuple.
    
    Parameters:
    tup (tuple): Input tuple
    lst (list): Input list
    
    Returns:
    int: Total count of elements from the list present in the tuple
    '''
    counts = Counter(tup)
    total_count = sum(counts[key] for key in lst)
    
    return total_count

# Test cases




def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)