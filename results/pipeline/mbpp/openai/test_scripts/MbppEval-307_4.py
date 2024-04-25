from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    updated_tuple = deepcopy(tuplex)
    
    if m < len(updated_tuple):
        updated_tuple_lst = list(updated_tuple)
        updated_tuple_lst[m].append(n)
        return tuple(updated_tuple_lst)
    else:
        return updated_tuple

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)