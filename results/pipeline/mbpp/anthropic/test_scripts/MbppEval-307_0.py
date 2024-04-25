from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    modified_tuple = deepcopy(tuplex)
    if isinstance(modified_tuple[m], list):
        modified_tuple[m] = [n]
    else:
        modified_tuple = tuple(modified_tuple[:m] + (modified_tuple[m],) + modified_tuple[m+1:])
    return modified_tuple

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)