def unique_sublists(list1):
    """
    Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurrences in the original list.

    Examples:
    unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']]) == {('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]]) == {(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
    """
    result = {}
    for sub_list in list1:
        sub_list_tuple = tuple(sub_list)
        if sub_list_tuple in result:
            result[sub_list_tuple] += 1
        else:
            result[sub_list_tuple] = 1
    return result

def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[10, 20, 30, 40], [60, 70, 50, 50], [90, 100, 200]])=={(10, 20, 30, 40): 1, (60, 70, 50, 50): 1, (90, 100, 200): 1}
    assert unique_sublists([['john']])=={('john',): 1}

check(unique_sublists)