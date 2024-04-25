from collections import Counter

def count_Occurrence(tup, lst):
    # Count the occurrences of each element in the tuple
    tup_counter = Counter(tup)
    
    # Initialize the total count to 0
    total_count = 0
    
    # Iterate over the elements in the list
    for elem in lst:
        # Add the count of the element to the total count
        total_count += tup_counter.get(elem, 0)
    
    return total_count

# Test the function with the given examples




def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2

check(count_Occurrence)