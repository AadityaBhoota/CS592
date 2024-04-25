from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    if m < 0 or m >= len(tuplex):
        raise IndexError("Index out of range")
    
    new_tuple = deepcopy(tuplex)
    element_at_m = new_tuple[m]
    
    if isinstance(element_at_m, list):
        new_tuple = new_tuple[:m] + (element_at_m[:n] + [n] + element_at_m[n+1:],) + new_tuple[m+1:]
    else:
        new_tuple = new_tuple[:m] + ([n],) + new_tuple[m+1:]
    
    return new_tuple

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)