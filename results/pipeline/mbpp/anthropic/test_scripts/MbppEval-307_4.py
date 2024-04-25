from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    new_tuplex = deepcopy(tuplex)
    new_tuplex[m][0] = n
    return new_tuplex

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)