def max_sum_list(lists):
    """
    Finds the list in a list of lists whose sum of elements is the highest.

    Args:
        lists (list): A list of lists, where each inner list contains integers.

    Returns:
        list: The list from the input list of lists with the highest sum of elements.
    """
    if not lists:
        return []

    max_sum = 0
    max_list = None

    for l in lists:
        curr_sum = sum(l)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_list = l

    return max_list

def check(candidate):
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]
    assert max_sum_list([[2,3,1]])==[2,3,1]

check(max_sum_list)