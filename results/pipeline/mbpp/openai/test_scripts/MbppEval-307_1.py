from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    tup_list = list(tuplex)
    
    if m < 0 or m >= len(tup_list):
        return tuple(tup_list)
    
    tup_list[m] = [n]
    return tuple(tup_list)

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)