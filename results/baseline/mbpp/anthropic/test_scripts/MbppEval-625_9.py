def swap_List(new_list):
    """
    Interchanges the first and last element in a given list.

    Args:
        new_list (list): The input list.

    Returns:
        list: The list with the first and last elements swapped.
    """
    if len(new_list) >= 2:
        new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)