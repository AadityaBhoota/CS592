def group_tuples(Input): 
    grouped = {}
    for tup in Input:
        if tup[0] in grouped:
            grouped[tup[0]].append(tup[1])
        else:
            grouped[tup[0]] = [tup[1]]
    
    output = [(key,) + tuple(val) for key, val in grouped.items()]
    return output

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)