def max_length_list(input_list):
    """
    Write a function to find the list with maximum length.

    Examples:
    max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
    max_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]]) == (5,[1,2,3,4,5])
    max_length_list([[3,4,5],[6,7,8,9],[10,11,12]]) == (4,[6,7,8,9])
    """
    if not isinstance(input_list, list) or not all(isinstance(inner_list, list) for inner_list in input_list):
        raise ValueError("Input must be a list of lists")

    max_length = 0
    max_list = []

    for inner_list in input_list:
        if len(inner_list) > max_length:
            max_length = len(inner_list)
            max_list = inner_list

    return max_length, max_list

def check(candidate):
    assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length_list([[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]])==(5,[1,2,3,4,5])
    assert max_length_list([[3,4,5],[6,7,8,9],[10,11,12]])==(4,[6,7,8,9])

check(max_length_list)