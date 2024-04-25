def count_list(input_list):
    """
    Write a python function to count the number of lists in a given number of lists.

    Examples:
    count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    count_list([[1,2],[2,3],[4,5]]) == 3
    count_list([[1,0],[2,0]]) == 2
    """
    return sum(1 for element in input_list if isinstance(element, list))

def check(candidate):
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4
    assert count_list([[1,2],[2,3],[4,5]]) == 3
    assert count_list([[1,0],[2,0]]) == 2

check(count_list)