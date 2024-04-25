def group_tuples(Input): 
    grouped_tuples = {}
    for tup in Input:
        key = tup[0]
        if key in grouped_tuples:
            grouped_tuples[key].append(tup[1])
        else:
            grouped_tuples[key] = [tup[1]]

    result = [(key, *items) for key, items in grouped_tuples.items()]

    return result

# Test cases




def check(candidate):
    assert group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]) == [('x', 'y', 'z'), ('w', 't')]
    assert group_tuples([('a', 'b'), ('a', 'c'), ('d', 'e')]) == [('a', 'b', 'c'), ('d', 'e')]
    assert group_tuples([('f', 'g'), ('f', 'g'), ('h', 'i')]) == [('f', 'g', 'g'), ('h', 'i')]

check(group_tuples)