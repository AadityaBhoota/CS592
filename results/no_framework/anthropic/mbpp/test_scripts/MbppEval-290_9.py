def max_length(list1):
    """
    Find the list of maximum length in a list of lists.

    Args:
        list1 (list): A list of lists.

    Returns:
        tuple: A tuple containing the length of the longest list and the longest list itself.
    """
    # Initialize variables to keep track of the longest list and its length
    longest_length = 0
    longest_list = None

    # Iterate through the input list
    for lst in list1:
        # Check if the current list is longer than the current longest list
        if len(lst) > longest_length:
            longest_length = len(lst)
            longest_list = lst

    return (longest_length, longest_list)

def check(candidate):
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert max_length([[5], [15,20,25]])==(3, [15,20,25])

check(max_length)