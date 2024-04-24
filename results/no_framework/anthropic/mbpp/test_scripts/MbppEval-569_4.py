def sort_sublists(list1):
    """
    Write a function to sort each sublist of strings in a given list of lists.

    Examples:
    sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']]) == [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']]) == [['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]
    """
    sorted_list = []
    for sublist in list1:
        sorted_sublist = sorted(sublist)
        sorted_list.append(sorted_sublist)
    return sorted_list

def check(candidate):
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])==[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    assert sort_sublists([['a','b'],['d','c'],['g','h'] , ['f','e']])==[['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]

check(sort_sublists)