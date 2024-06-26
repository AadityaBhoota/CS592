from itertools import groupby

def pack_consecutive_duplicates(list1):
    """
    Write a function to pack consecutive duplicates of a given list elements into sublists.

    Examples:
    pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd']) == [['a', 'a'], ['b'], ['c'], ['d', 'd']]
    """
    result = []
    for _, group in groupby(list1):
        group_list = list(group)
        result.append(group_list)
    return result

def check(candidate):
    assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]

check(pack_consecutive_duplicates)