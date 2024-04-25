from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    if m < 0 or m >= len(tuplex):
        return "Invalid index for the given tuple"
    
    tuplex_copy = deepcopy(tuplex)
    tuplex_copy[m] = [n]
    
    return tuple(tuplex_copy)

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)