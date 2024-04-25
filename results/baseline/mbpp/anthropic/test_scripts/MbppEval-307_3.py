from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    """
    Write a function to get a colon of a tuple.

    Examples:
    colon_tuplex(("HELLO", 5, [], True) ,2,50) == ("HELLO", 5, [50], True)
    colon_tuplex(("HELLO", 5, [], True) ,2,100) == (("HELLO", 5, [100],True))
    colon_tuplex(("HELLO", 5, [], True) ,2,500) == ("HELLO", 5, [500], True)
    """
    # Create a deep copy of the tuple to avoid modifying the original
    new_tuple = deepcopy(tuplex)

    # Check if the index m is within the bounds of the tuple
    if m >= 0 and m < len(new_tuple):
        # Modify the element at index m
        if isinstance(new_tuple[m], list):
            new_tuple[m] = [n]
        else:
            new_tuple = new_tuple[:m] + (new_tuple[m],) + new_tuple[m+1:]
            new_tuple = new_tuple[:m] + (n,) + new_tuple[m+1:]

    return new_tuple

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)