def colon_tuplex(tuplex, m, n):
    # convert the tuple to a list so we can modify it
    tup_list = list(tuplex)

    # check if the index m is within the range of the tuple
    if m < len(tup_list):
        # update the element at index m with n wrapped in a list
        tup_list[m] = [n]

    # convert the modified list back to a tuple
    new_tuplex = tuple(tup_list)
    
    return new_tuplex

# Test cases




def check(candidate):
    assert colon_tuplex(("HELLO", 5, [], True) ,2,50)==("HELLO", 5, [50], True)
    assert colon_tuplex(("HELLO", 5, [], True) ,2,100)==(("HELLO", 5, [100],True))
    assert colon_tuplex(("HELLO", 5, [], True) ,2,500)==("HELLO", 5, [500], True)

check(colon_tuplex)