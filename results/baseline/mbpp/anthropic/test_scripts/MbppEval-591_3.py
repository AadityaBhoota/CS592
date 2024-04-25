def swap_List(new_list):
    """
    Interchanges the first and last elements in a list.

    Args:
        new_list (list): The input list.

    Returns:
        list: The modified list with the first and last elements swapped.
    """
    if len(new_list) < 2:
        return new_list

    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

def check(candidate):
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert swap_List([1, 2, 3]) == [3, 2, 1]
    assert swap_List([4, 5, 6]) == [6, 5, 4]

check(swap_List)