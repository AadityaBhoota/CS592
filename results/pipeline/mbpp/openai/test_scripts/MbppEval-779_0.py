def unique_sublists(list1):
    unique_dict = {}
    
    for sublist in list1:
        sublist_tuple = tuple(sublist)
        
        if sublist_tuple in unique_dict:
            unique_dict[sublist_tuple] += 1
        else:
            unique_dict[sublist_tuple] = 1
    
    return unique_dict

def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}

check(unique_sublists)