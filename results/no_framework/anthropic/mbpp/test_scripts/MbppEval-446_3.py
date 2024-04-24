from collections import Counter

def count_Occurrence(tup, lst):
    """
    Counts the occurrence of all elements of the list 'lst' in the tuple 'tup'.

    Args:
        tup (tuple): The input tuple.
        lst (list): The list of elements to count.

    Returns:
        int: The total count of the elements in the list 'lst' that are present in the tuple 'tup'.
    """
    # Convert the tuple to a list
    tup_list = list(tup)
    
    # Use Counter to count the occurrences of each element in the list
    tup_count = Counter(tup_list)
    
    # Count the occurrences of the elements in the given list
    total_count = sum(tup_count[item] for item in lst)
    
    return total_count

def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)