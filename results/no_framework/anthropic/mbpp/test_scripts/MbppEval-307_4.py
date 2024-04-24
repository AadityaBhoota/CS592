from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    """
    Write a function to get a colon of a tuple.

    Examples:
    colon_tuplex(("HELLO", 5, [], True) ,2,50) == ("HELLO", 5, [50], True)
    colon_tuplex(("HELLO", 5, [], True) ,2,100) == (("HELLO", 5, [100],True))
    colon_tuplex(("HELLO", 5, [], True) ,2,500) == ("HELLO", 5, [500], True)
    """
    new_tuplex = list(deepcopy(tuplex))
    if m >= len(new_tuplex):
        return tuplex
    elif isinstance(new_tuplex[m], list):
        new_tuplex[m] = [n]
    else:
        new_tuplex[m] = (new_tuplex[m],)
        new_tuplex[m][0] = n
    return tuple(new_tuplex)

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)