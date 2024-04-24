def colon_tuplex(tuplex, m, n):
    if m < len(tuplex):
        new_tuple = list(tuplex)
        if isinstance(new_tuple[m], list):
            new_tuple[m].append(n)
        else:
            new_tuple[m] = [n]
        return tuple(new_tuple)
    return tuplex

# Test the function with the provided examples




def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)