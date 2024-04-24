def unique_sublists(list1):
    """
    Write a function to count the number of lists within a list. The function should return a dictionary, where every list is turned to a tuple, and the value of the tuple is the number of its occurrences.

    Examples:
    unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']]) == {('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]]) == {(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}
    """
    count_dict = {}
    for sublst in list1:
        sublst = tuple(sublst)
        if sublst in count_dict:
            count_dict[sublst] += 1
        else:
            count_dict[sublst] = 1
    return count_dict

def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}

check(unique_sublists)