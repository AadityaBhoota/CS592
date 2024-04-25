from collections import Counter

def count_Occurrence(tup, lst):
    '''
    Write a python function to count the occurrence of all elements of list in a tuple.

    Examples:
    count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    count_Occurrence((1,2,3,4,5,6),[1,2]) == 2
    '''
    # Convert the tuple to a list to make it mutable
    tup_list = list(tup)
    
    # Use Counter to count the occurrences of the elements in the list
    counter = Counter(tup_list)
    
    # Initialize the total count to 0
    total_count = 0
    
    # Iterate through the given list and add the count of each element to the total count
    for item in lst:
        total_count += counter[item]
    
    return total_count

def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)