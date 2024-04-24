def colon_tuplex(tuplex, m, n):
    new_tuplex = list(tuplex)
    new_tuplex[m] = new_tuplex[m] + [n]
    return tuple(new_tuplex)

# Test cases




def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)