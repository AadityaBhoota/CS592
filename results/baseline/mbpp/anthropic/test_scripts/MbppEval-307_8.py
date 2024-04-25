from copy import deepcopy

def colon_tuplex(tuplex, m, n):
    """
    Write a function to get a colon of a tuple.

    Examples:
    colon_tuplex(("HELLO", 5, [], True), 2, 50) == ("HELLO", 5, [50], True)
    colon_tuplex(("HELLO", 5, [], True), 2, 100) == ("HELLO", 5, [100], True)
    colon_tuplex(("HELLO", 5, [], True), 2, 500) == ("HELLO", 5, [500], True)
    """
    
    # Create a deep copy of the input tuple
    result = deepcopy(tuplex)
    
    # Check if the third element is a list
    if isinstance(result[2], list):
        # Modify the third element of the tuple
        result[2][0] = n
    else:
        # Create a new list with the given value
        result[2] = [n]
    
    return result

def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)