def remove_elements(list1, list2):
    """
    Write a function to remove all elements from a given list present in another list.

    Examples:
    remove_elements([1,2,3,4,5,6,7,8,9,10],[2,4,6,8]) == [1, 3, 5, 7, 9, 10]
    remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
    remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7]) == [1, 2, 3, 4, 6, 8, 9, 10]
    """
    return [item for item in list1 if item not in list2]

def check(candidate):
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]

check(remove_elements)