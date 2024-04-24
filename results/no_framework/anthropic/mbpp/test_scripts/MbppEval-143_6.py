def find_lists(Input):
    """
    Write a function to find the number of lists present in the given tuple.

    Examples:
    find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    find_lists(([1, 2], [3, 4], [5, 6])) == 3
    find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1
    """
    return sum(1 for element in Input if isinstance(element, list))

def check(candidate):
    assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert find_lists(([1, 2], [3, 4], [5, 6]))  == 3
    assert find_lists(([9, 8, 7, 6, 5, 4, 3, 2, 1])) == 1

check(find_lists)