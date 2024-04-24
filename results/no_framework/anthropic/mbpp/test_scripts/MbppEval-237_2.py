from collections import Counter

def check_occurrences(test_list):
    """
    Counts the occurrences of each unique tuple in the input list.
    
    Args:
        test_list (list): A list of tuples.
    
    Returns:
        dict: A dictionary where the keys are the unique tuples and the values are the number of times each tuple appears in the input list.
    """
    # Create a Counter object to count the occurrences of each tuple
    tuple_counter = Counter(test_list)
    
    # Convert the Counter object to a dictionary and return it
    return dict(tuple_counter)

def check(candidate):
    assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}

check(check_occurences)