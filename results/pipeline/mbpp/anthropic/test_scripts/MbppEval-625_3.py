def swap_List(newList):
    """
    Write a python function to interchange the first and last element in a given list.

    Examples:
    swap_List([1,2,3]) == [3,2,1]
    swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    swap_List([4,5,6]) == [6,5,4]
    swap_List([1]) == [1]
    swap_List([]) == []
    """
    if len(newList) < 2:
        return newList
    return [newList[-1]] + newList[1:-1] + [newList[0]]

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]

check(swap_List)